from django.contrib import admin
from .models import TypeVechicle, SlotVechicle, ParkingSpot, EntryDetails

admin.site.register(ParkingSpot)
admin.site.register(EntryDetails)

class ParkingSpot(admin.ModelAdmin):
    list_filter = ('spot_number', 'spot_number')
    list_display = ('spot_number', 'spot_number', 'is_occupied')
