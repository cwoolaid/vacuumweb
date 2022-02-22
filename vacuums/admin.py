from django.contrib import admin
from .models import Type, Brand, Model, InventoryNumber, Country

# Register your models here.

admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(InventoryNumber)
admin.site.register(Country)
