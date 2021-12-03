from rest_framework import serializers
from AuthApp.models.user import User
from AuthApp.models.passenger import Passenger
from AuthApp.models.car import Car
from AuthApp.models.driver import Driver

from AuthApp.serializers.passengerSerializer import PassengerSerializer
from AuthApp.serializers.carSerializer import CarSerializer
from AuthApp.serializers.driverSerializer import DriverSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'created_at', 'email', 'typeAccount']
 
    def to_representation (self, obj):
        user = User.objects.get(id = obj.id)
        return{
            'username':user.username,
            'email':user.email,
            'created_at': user.created_at,
            'typeAccount':user.typeAccount
        }

class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'typeAccount']

class UserPassengerSerializer(serializers.ModelSerializer):
    account = PassengerSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'typeAccount', 'account']

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        user = User.objects.create(**validated_data)
        Passenger.objects.create(user=user, **account_data)
        return user

    def to_representation(self, objUser):
        user = User.objects.get(id=objUser.id)
        account = Passenger.objects.get(user=objUser)
        infoUser = {
            'id': user.id,
            'username': user.username,
            'typeAccount': user.typeAccount,
            'email': user.email,
            'account': {
                'id': account.id,
                'name': account.name,
                'lastName': account.lastName,
                'city': account.city,
                'birthDate': account.birthDate,
                'gender': account.gender,
                'documentNumber': account.documentNumber,
                'phoneNumber': account.phoneNumber
            }
        }
        return infoUser

class UserDriverSerializer(serializers.ModelSerializer):
    account = DriverSerializer()
    car = CarSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'typeAccount', 'account', 'car']

    def to_representation(self, objUser):
        user = User.objects.get(id=objUser.id)
        account = Driver.objects.get(user=objUser)
        car = Car.objects.get(objUser)
        infoUser = {
            'id': user.id,
            'username': user.username,
            'typeAccount': user.typeAccount,
            'email': user.email,
            'account': {
                'id': account.id,
                'name': account.name,
                'lastName': account.lastName,
                'city': account.city,
                'birthDate': account.birthDate,
                'gender': account.gender,
                'documentNumber': account.documentNumber,
                'licenseNumber': account.licenseNumber,
                'phoneNumber': account.phoneNumber,
                # 'car': {
                #     "carRegistrationNumber": car.carRegistrationNumber,
                #     "cityRegistration": car.cityRegistration,
                #     "color": car.color,
                #     "type": car.type,
                #     "brand": car.brand,
                #     "description": car.description,
                #     "equipment": car.equipment,
                # }
            }
        }
        return infoUser
