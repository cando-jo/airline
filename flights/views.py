from django.shortcuts import render
from .models import Flight, Airport
# Create your views here.

def index(request):
    all_flights = Flight.objects.all()
    return render(request, 'flights/index.html', {
        'all_flights': all_flights
    })


def add_flight(request):
    if request.method == "POST":
        origin = request.POST.get("added_flight_origin")
        destination = request.POST.get("added_flight_destination")
        duration = request.POST.get("added_flight_duration")
        f = Flight(origin, destination, duration)
        