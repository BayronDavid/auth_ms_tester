from django.db import models

class Car (models.Model):
    id = models.BigAutoField(primary_key=True)
    carRegistrationNumber = models.CharField( max_length=20)  # numero del carro PK
    cityRegistration = models.CharField(max_length=60)  # Ciudad de registro
    color = models.CharField(max_length=60)  # Tipo del carro
    brand = models.CharField(max_length=60)  # Marca del carro
    model = models.CharField(max_length=60)  # Modelo del carro
    description = models.CharField(max_length=255, blank=True)  # Descripcion del carro
    equipment = models.CharField(max_length=40, choices=(
        ('PU', 'Pick Up'),  # Camioneta pick up con platon
        ('T', 'Con Trunk'),  # Carro con baul
        ('NT', 'Sin Trunk')  # Carro sin baul
    ))

