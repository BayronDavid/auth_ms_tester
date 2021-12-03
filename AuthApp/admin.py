from django.contrib import admin
from .models.user import User
from .models.driver import Driver
from .models.car import Car
from .models.passenger import Passenger

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Passenger)
