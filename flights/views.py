from django.shortcuts import render
from .models import Flight, Airport, Passenger
# Create your views here.

def index(request):
    all_flights = Flight.objects.all()
    return render(request, 'flights/index.html', {
        'all_flights': all_flights
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, 'flights/flight.html', {
        'flight': flight,
        'passengers': flight.passengers.all()
    })
        