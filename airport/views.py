from django.shortcuts import render

# Create your views here.
import requests
import configparser
import os
from geopy.geocoders import Nominatim


# # Create your views here.
class AirportTracker:
    """Class to return valid airport with latitude and longitude"""

    def __init__(self, place, country_code):
        self.place = place
        self.country_code = country_code
        self.place_type = None
        self.url = None
        self.params = None
        airport_config = configparser.ConfigParser()
        airport_config.read(os.path.join(os.path.dirname(__file__), 'conf.ini'))
        self.airport_by_radius_url = airport_config.get('Airport', 'airport_by_radius')
        self.airport_by_name_url = airport_config.get('Airport', 'airport_by_name')
        self.nearest_airport_url = airport_config.get('Airport', 'nearest_airport')
        self.airport_by_code_url = airport_config.get('Airport', 'airport_by_code')
        self.rapidapi_host_name = airport_config.get('Airport', 'rapidapi_host_name')
        self.rapidapi_host_value = airport_config.get('Airport', 'rapidapi_host_value')
        self.rapidapi_key_name = airport_config.get('Airport', 'rapidapi_key_name')
        self.rapidapi_key_value = airport_config.get('Airport', 'rapidapi_key_value')
        self.radius = airport_config.get('Airport', 'radius')
        self.headers = {self.rapidapi_host_name: self.rapidapi_host_value,
                        self.rapidapi_key_name: self.rapidapi_key_value, 'Content-Type': 'application/json'}

    def get_airport_by_name(self):
        """Return airport if name is given instead of airport code.
        If no airport found it looks for nearest airport in radius of x kms"""

        self.place_type = 'name'
        self._set_url_params(place_type=self.place_type)
        response = self.http_request()
        if response:
            for record in response:
                if record['city'].lower() == self.place.lower() and record['countryCode'] == self.country_code:
                    return record
            raise ValueError('Invalid place. Please enter correct value')
        else:
            lat, long = self.get_lat_long(place=self.place)
            response = self.get_airports_by_radius(lat=lat, long=long, radius=self.radius)
            return response

    @staticmethod
    def get_lat_long(place=None):
        """ Return latitude longitude for a place based on name """

        geolocator = Nominatim(user_agent="Firefox")
        location = geolocator.geocode(place)
        if location:
            latitude, longitude = (location.latitude, location.longitude)
            return latitude, longitude
        else:
            raise PlaceNotFoundException('Could not locate lat long for the place')

    def get_airport_by_code(self):
        """Returns airport based on airport code"""

        self.place_type = 'code'
        self._set_url_params(place_type=self.place_type)
        response = self.http_request()
        return response

    def get_airports_by_radius(self, lat=None, long=None, radius=0):
        """Returns airports in radius of <radius> km. Input required latitude and longitude"""

        if lat is not None and long is not None:
            self._set_url_params(lat=lat, long=long, radius=radius)
            response = self.http_request()
            return response

    def _set_url_params(self, place_type=None, lat=None, long=None, radius=None):
        if lat is not None and long is not None and radius is not None:
            self.url = self.airport_by_radius_url
            self.params = {"radius": radius, "lng": long, "lat": lat}
        else:
            if place_type == 'code':
                self.url = self.airport_by_code_url
                self.params = {"code": self.place}
            elif place_type == 'name':
                self.url = self.airport_by_name_url
                self.params = {"text": self.place}

    def http_request(self):
        """Run a http request and return response"""

        try:
            response = requests.request("GET", self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.Timeout as e:
            print(f'Request timed out. Reason - {e}')
        except requests.exceptions.RequestException as e:
            print(f'Error while making request. Error - {e}')

    def __call__(self, *args, **kwargs):
        if len(self.place) == 3:
            return self.get_airport_by_code()
        elif len(self.place) > 3:
            return self.get_airport_by_name()
        else:
            raise ValueError('Invalid place name. Please enter either code or full name')


class PlaceNotFoundException(Exception):
    pass

# a = AirportTracker(place='latur', country_code='IN')
# print(a())
