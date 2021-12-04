from django.contrib import admin
from .models.user import User
from .models.car import Car

admin.site.register(User)
admin.site.register(Car)
