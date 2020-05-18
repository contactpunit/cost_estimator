from django.shortcuts import render

# Create your views here.
import requests
import configparser
import os
import sys


#
# # Create your views here.
class AirportTracker:
    def __init__(self, **kwargs):
        self.place = kwargs.get('place', None)
        self.country_code = kwargs.get('country_code', None)
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
        self.headers = {self.rapidapi_host_name: self.rapidapi_host_value,
                        self.rapidapi_key_name: self.rapidapi_key_value, 'Content-Type': 'application/json'}

    def get_airport_by_name(self):
        self.place_type = 'name'
        self._set_url_params()
        response = self.http_request()
        if response:
            for record in response:
                if record['name'] == self.place and record['countryCode'] == self.country_code:
                    return record
            raise ValueError('Invalid place. Please enter correct value')
        if not response:
            self.get_airports_by_radius(radius=200, longitude=)
        return response

    def get_airport_by_code(self):
        self.place_type = 'code'
        self._set_url_params()
        response = self.http_request()
        return response

    def get_nearest_airports(self):
        pass

    def get_airports_by_radius(self):
        pass

    def _set_url_params(self):
        if self.place_type == 'code':
            self.url = self.airport_by_code_url
            self.params = {"code": self.place}
        elif self.place_type == 'name':
            self.url = self.airport_by_name_url
            self.params = {"text": self.place}

    def http_request(self):
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
            self.get_airport_by_code()
        elif len(self.place) > 3:
            self.get_airport_by_name()
        else:
            raise ValueError('Invalid place name. Please enter either code or full name')


a = AirportTracker(place='latur', country_code='IN')
print(a())
