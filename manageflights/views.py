from django.shortcuts import render

# Create your views here.
class FlightTracker:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
