from rest_framework import serializers
from AuthApp.models import User, Car

from .carSerializer import CarSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'lastName', 'birthDate', 'gender', 'documentNumber', 'phoneNumber', 'typeAccount']
 
    def to_representation (self, obj):
        user = User.objects.get(id = obj.id)
        return{
            'username':user.username,
            'email':user.email,
            'name':user.name,
            'lastName':user.lastName,
            'birthDate': user.birthDate,
            'gender':user.gender,
            'documentNumber': user.documentNumber,
            'phoneNumber': user.phoneNumber,
            'typeAccount':user.typeAccount,
        }

class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'typeAccount']

class UserDriverSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email','name', 'lastName', 'birthDate', 'gender', 'documentNumber', 'phoneNumber', 'typeAccount', 'car']

    def to_representation(self, objUser):
        user = User.objects.get(id=objUser.id)
        car = Car.objects.get(user=objUser)
        return {
            'username':user.username,
            'email':user.email,
            'name':user.name,
            'lastName':user.lastName,
            'birthDate': user.birthDate,
            'gender':user.gender,
            'documentNumber': user.documentNumber,
            'phoneNumber': user.phoneNumber,
            'typeAccount':user.typeAccount,
            'car': {
                'licenseNumber': car.licenseNumber,
                "carRegistrationNumber": car.carRegistrationNumber,
                "color": car.color,
                "brand": car.brand,
                'model': car.model,
                "description": car.description,
                "equipament": car.equipament,
            }
        }
