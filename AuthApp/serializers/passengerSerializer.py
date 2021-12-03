from rest_framework import serializers
from AuthApp.models.passenger import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'lastName', 'city', 'birthDate','gender', 'documentNumber', 'phoneNumber']


