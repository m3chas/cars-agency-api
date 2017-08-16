from django.contrib import admin
from .models import Brand, Manufacturer, Model, Car


# Creating admin models
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'manufacturer', 'model', 'trim' , 'year')
    list_filter = ('brand', 'manufacturer', 'model')


# Register your models here.
admin.site.register(Brand)
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Car, CarAdmin)
