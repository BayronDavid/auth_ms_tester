from rest_framework import serializers
from AuthApp.models.driver import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'lastName', 'city', 'birthDate', 'gender','documentNumber', 'licenseNumber', 'phoneNumber', 'car']

class AllDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'lastName', 'gender','documentNumber', 'licenseNumber', 'phoneNumber',  'car']
