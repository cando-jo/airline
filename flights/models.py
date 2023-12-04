from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=4)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
    
class Flight(models.Model):
    # related name to access an Airport object's flights (ex: Airport obj with id 1's flights)
    # ---- because we can't directly say Airport_obj.origin, since it's not an airport field, but 
    # ---- now we can say Airport_obj.departures or Airport_obj.arrivals
    # models.CASCADE makes sure if an airport gets deleted from the database it also delets all the flights 
    # --- which has that airport as an origin
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: from {self.origin} to {self.destination}"
    
    
class Passenger(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.first} {self.last} on flight {self.flights}"
    