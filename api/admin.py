from django.contrib import admin
from . models import Category,City,Country,Products,State,User,Brand
# Register your models here.

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Products)
admin.site.register(State)
admin.site.register(User)
admin.site.register(Brand)
