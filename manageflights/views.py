from django.shortcuts import render


# Create your views here.
class FlightTracker:
    def __init__(self, source, s_country, destination, d_country, num_travellers):
        self.source = source
        self.destination = destination
        self.source_country = s_country
        self.dest_country = d_country
        self.num_travellers = num_travellers

    def __repr__(self):
        return f'({self.__class__.__name__}) from {self.source} to {self.destination} for {self.num_travellers} travellers'
