from AuthApp.models import Passenger
from AuthApp.serializers import PassengerSerializer
from rest_framework import generics

class PassengerListCreateView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

#Retrieve Update and Delete
class PassengerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class AllPassengersView(generics.ListAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
