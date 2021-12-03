from AuthApp.models import Driver
from AuthApp.serializers import DriverSerializer, AllUsersSerializer
from rest_framework import generics


class DriverListCreateView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

#Retrieve Update and Delete 
class DriverRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class AllDriversView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = AllUsersSerializer
