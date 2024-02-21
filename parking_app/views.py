from django.shortcuts import render
from .models import ParkingSpot, EntryDetails
from django.utils import timezone
from django.shortcuts import render, redirect
# Create your views here.
def parking_lot(request):
    spots = ParkingSpot.objects.all()
    return render(request, 'parking_app/parking_lot.html', {'spots': spots})

def exit_car(request, spot_id):
    spot = ParkingSpot.objects.get(pk=spot_id)
    print(spot)
    total_sec = 0
    total_hr = 0 
    total_price = 0
    type_vehicle_price = 20
    if spot.Type_number == 2:
        total_price = type_vehicle_price = 60
    if spot.Type_number == 3:
        total_price = type_vehicle_price = 100
    if spot.is_occupied:
        total_hr = abs(spot.created - timezone.now()).total_seconds() / 3600.0
        total_hr = int(total_hr)
        total_min = abs(spot.created - timezone.now()).total_seconds() / 60
        total_min = int(total_min)
        total_days = abs(spot.created - timezone.now()).total_seconds() / 86400
        total_days = int(total_days)
        if(total_min <= 60):
            print('1')
            total_price = type_vehicle_price
        elif(total_hr < 24):
            print('2')
            total_price = type_vehicle_price * total_hr
        elif(total_hr > 24): 
            print('3')
            total_price = type_vehicle_price * total_hr
            total_price = total_price + 5000
        else:
            print('4')
            total_price = type_vehicle_price * total_hr
            price_total_days = total_days * 5000
            total_price = total_price + price_total_days
    return render(request, 'parking_app/exit.html', {'spot': spot, 'total_hrs': int(total_hr), 'total_price': total_price })

def verify_payment(request, spot_id):
    spot = ParkingSpot.objects.get(pk=spot_id)
    if request.method == 'POST':
        payment = request.POST['payment']
        total_hr = 0 
        total_price = 0
        type_vehicle_price = 20
        if spot.Type_number == 2:
            total_price = type_vehicle_price = 60
        if spot.Type_number == 3:
            total_price = type_vehicle_price = 100
        if spot.is_occupied:
            total_hr = abs(spot.created - timezone.now()).total_seconds() / 3600.0
            total_hr = int(total_hr)
            total_min = abs(spot.created - timezone.now()).total_seconds() / 60
            total_min = int(total_min)
            total_days = abs(spot.created - timezone.now()).total_seconds() / 86400
            total_days = int(total_days)
            if(total_min <= 60):
                total_price = type_vehicle_price
            elif(total_hr < 24):
                total_price = type_vehicle_price * total_hr
            elif(total_hr > 24): 
                total_price = type_vehicle_price * total_hr
                total_price = total_price + 5000
            else:
                total_price = type_vehicle_price * total_hr
                price_total_days = total_days * 5000
                total_price = total_price + price_total_days
        if(int(total_price) <= int(payment)):
            spot.car.exit_time = timezone.now()
            spot.is_occupied = False
            spot.save()
            exchange_fare = int(payment) - int(total_price)
            if(exchange_fare > 0):
                return render(request, 'parking_app/greet.html', {'message': "Here's your exchange fare {}, Thank you Please park us again".format(exchange_fare)})
            else:
                return render(request, 'parking_app/greet.html', {'message': "Thank you Please park us again"})
        else:
            return render(request, 'parking_app/insufficient.html')
def insufficient(request):
    return redirect('parking_lot')
def enter_car(request, spot_id):
    spot = ParkingSpot.objects.get(pk=spot_id)
    return render(request, 'parking_app/fillup_entry.html', {'spot': spot })

def entry_vehicle(request, spot_id):
    if request.method == 'POST':
        selected_car_type = request.POST.get('type')
        spot = ParkingSpot.objects.get(pk=spot_id)
        car = EntryDetails.objects.create(entry_time=timezone.now())
        spot.parkingslot = car
        spot.Type_number = int(selected_car_type)
        spot.is_occupied = True
        spot.save()
        return redirect('parking_lot')

