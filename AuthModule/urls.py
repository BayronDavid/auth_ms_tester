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
    #Car
    path('car/', views.CarListCreateView.as_view()),
    path('car/', views.CarRetrieveUpdateDeleteView.as_view()),
]
