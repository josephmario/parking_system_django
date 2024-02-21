from django.db import models
from django.utils import timezone
# Create your models here.


SLOT_VEHICLE =( 
        (1, "1st Slot"), 
        (2, "2nd Slot"), 
        (3, "3rd Slot"), 
    ) 
TYPE_VEHICLE =( 
        (1, "SMALL"), 
        (2, "MEDIUM"), 
        (3, "LARGE"), 
    ) 
class TypeVechicle(models.Model):
    
    id = models.AutoField(primary_key=True)
    type = models.IntegerField(choices=TYPE_VEHICLE)
    modified = models.DateTimeField() 
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TypeVechicle, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.type)

class SlotVechicle(models.Model):
    
    id = models.AutoField(primary_key=True)
    slot = models.IntegerField(choices=SLOT_VEHICLE)
    modified = models.DateTimeField() 
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SlotVechicle, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.slot)
    
class EntryDetails(models.Model):
    license_plate = models.CharField(max_length=15)
    entry_time = models.DateTimeField(null=True, blank=True)
    exit_time = models.DateTimeField(null=True, blank=True)

class ParkingSpot(models.Model):
    spot_number = models.IntegerField()
    id = models.AutoField(primary_key=True)
    slot_number = models.IntegerField(choices=SLOT_VEHICLE, null=True, blank=True)
    Type_number = models.IntegerField(choices=TYPE_VEHICLE, null=True, blank=True)
    is_occupied = models.BooleanField(default=False)
    car = models.OneToOneField(EntryDetails, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(null=True)
    
    def __str__(self):
        return str(self.spot_number)
    
