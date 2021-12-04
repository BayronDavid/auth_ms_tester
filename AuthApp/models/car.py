from django.db import models
from .user import User

class Car (models.Model):
    id = models.AutoField(primary_key=True)
    licenseNumber = models.CharField(max_length=20, null=True)
    carRegistrationNumber = models.CharField( max_length=20)  # numero del carro PK
    color = models.CharField(max_length=60)  # Tipo del carro
    brand = models.CharField(max_length=60)  # Marca del carro
    model = models.CharField(max_length=60)  # Modelo del carro
    description = models.CharField(max_length=255, blank=True)  # Descripcion del carro
    equipament = models.CharField(max_length=40, choices=(
        ('PU', 'Pick Up'),  # Camioneta pick up con platon
        ('T', 'Con Trunk'),  # Carro con baul
        ('NT', 'Sin Trunk')  # Carro sin baul
    ))
    user = models.ForeignKey (User, on_delete=models.CASCADE )