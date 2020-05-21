from .airport_utils import AirportTracker
from .flight_utils import FlightTracker


class Travel:
    def __init__(self, source, destination, country, travel_date, num_passengers):
        self.source = source
        self.destination = destination
        self.country = country
        self.travel_date = travel_date
        self.num_passengers = int(num_passengers)

    def _find_country_code(self):
        pass

    def find_itineraries(self):
        source_airport = AirportTracker(place=self.source)
