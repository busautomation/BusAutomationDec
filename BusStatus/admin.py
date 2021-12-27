from django.contrib import admin
from .models import BusSatusData, SensorData

# Register your models here.

class BusSatusDataAdmin(admin.ModelAdmin):
    list_display = ('BusNo', 'DriverName', 'ConductorName',  'DriverContactNo', 'ConductorContactNo')
admin.site.register(BusSatusData, BusSatusDataAdmin)
admin.site.register(SensorData)