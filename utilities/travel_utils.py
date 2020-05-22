from .airport_utils import AirportTracker
from .flight_utils import FlightTracker
import pycountry
from .travelExceptions import *


class Travel:
    def __init__(self, source, destination, country, travel_date, num_passengers):
        self.source = source
        self.destination = destination
        self.country = country
        self.travel_date = travel_date
        self.num_passengers = int(num_passengers)
        if self.find_country_code():
            self.country = self.find_country_code()
        else:
            raise InvalidCountryException('Country not valid. Please enter either country code or correct country name')

    def find_country_code(self):
        if len(self.country) != 2:
            try:
                country = pycountry.countries.search_fuzzy(self.country)
                if len(country) > 1:
                    for entry in country:
                        if entry.name.lower() == self.country.lower():
                            return entry.alpha_2
                        else:
                            return country.alpha_2
            except LookupError:
                return None

    def find_airport(self, place):
        airport = AirportTracker(place=place, country_code=self.country)
        return airport()

    def find_itineraries(self):
        source_airport = self.find_airport(place=self.source)
        dest_airport = self.find_airport(place=self.destination)
        deviation = any([source_airport.get('nearest', None), dest_airport.get('nearest', None)])
        for srecord in source_airport['records']:
            for drecord in dest_airport['records']:
                if not srecord['code'] == drecord['code']:
                    f = FlightTracker(source=srecord['code'], destination=drecord['code'], country=self.country,
                                      travel_date=self.travel_date)
                    results = f.get_flights()
                    if results:
                        result = f.parse_results(results)
                        result['deviation'] = deviation
                        return result
        raise NoFlightsAvailableException('No Flights are available')

# c = Travel(source='latur', destination='delhi', country='india', travel_date='2020-06-01', num_passengers=2)
# print(c.find_itineraries())
