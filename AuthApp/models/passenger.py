from datetime import datetime
from django.db import models
from .user import User


class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    birthDate = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=40, choices=(
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ))
    documentNumber = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=60)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
