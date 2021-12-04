from rest_framework import serializers
from AuthApp.models.car import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'licenseNumber','carRegistrationNumber','color', 'brand','model','description', 'equipament']
