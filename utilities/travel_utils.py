from .airport_utils import AirportTracker
from .flight_utils import FlightTracker
import pycountry
from .travelExceptions import *


class Travel:
    def __init__(self, source, destination, country, travel_date, num_passengers):
        self.source = source
        self.destination = destination
        self.travel_date = travel_date
        self.num_passengers = int(num_passengers)
        if self.find_country_code(country):
            self.country = self.find_country_code(country)
        else:
            raise InvalidCountryException('Country not valid. Please enter either country code or correct country name')

    @staticmethod
    def find_country_code(country):
        try:
            if len(country) != 2:
                result = pycountry.countries.search_fuzzy(country)
                if len(result) > 1:
                    for entry in result:
                        if entry.name.lower() == country.lower() or entry.official_name.lower() == country.lower():
                            return entry.alpha_2
                else:
                    return result[0].alpha_2
            elif len(country) == 2:
                result = pycountry.countries.search_fuzzy(country)
                if result[0].alpha_2.lower() == country.lower():
                    return result[0].alpha_2
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
                        result.update({'source': self.source, 'destination': self.destination, 'country': self.country,
                                       'travel_date': self.travel_date})
                        return result
        raise NoFlightsAvailableException('No Flights are available')
