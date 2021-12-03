from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from AuthApp                        import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    #All Users/Passenger/Drivers
    path('users/', views.AllUsersView.as_view()),
    path('drivers/', views.AllDriversView.as_view()),
    path('passengers/', views.AllPassengersView.as_view()),
    #Car
    path('car/', views.CarListCreateView.as_view()),
    path('car/', views.CarRetrieveUpdateDeleteView.as_view()),
    #Driver
    path('driver/', views.DriverListCreateView.as_view()),
    path('driver/', views.DriverRetrieveUpdateDeleteView.as_view()),
    #Passenger
    path('passenger/', views.PassengerListCreateView.as_view()),
    path('passenger/', views.PassengerRetrieveUpdateDeleteView.as_view())
]
