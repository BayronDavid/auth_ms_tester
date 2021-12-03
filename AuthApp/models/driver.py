from datetime import datetime
from django.db import models
from .user import User
from .car import Car

class Driver (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=True)
    lastName = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=60, default='')
    birthDate = models.DateField(default = datetime.now)
    gender = models.CharField(max_length=40, null=True, choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ))
    documentNumber = models.CharField(max_length=20, null=True)
    licenseNumber = models.CharField(max_length=20, null=True)
    car = models.ForeignKey(
        Car,  # Modelo de carros
        related_name='car_driver',
        on_delete=models.CASCADE)
    phoneNumber = models.CharField (max_length=60, null=True )
    user = models.ForeignKey ( User, on_delete=models.CASCADE )
