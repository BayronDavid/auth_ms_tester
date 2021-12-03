from AuthApp.models import Car
from AuthApp.serializers import CarSerializer
from rest_framework import generics

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

#Retrieve Update and Delete
class CarRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
