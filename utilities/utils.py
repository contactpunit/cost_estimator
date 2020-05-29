# Create your views here.
import requests
import configparser
import os


class ConfigReaderMixin:
    config_reader = configparser.ConfigParser()
    config_reader.read(os.path.join(os.path.dirname(__file__), 'conf.ini'))

    @property
    def airport_by_radius_url(self):
        return self.config_reader.get('Airport', 'airport_by_radius')

    @property
    def airport_by_name_url(self):
        return self.config_reader.get('Airport', 'airport_by_name')

    @property
    def nearest_airport_url(self):
        return self.config_reader.get('Airport', 'nearest_airport')

    @property
    def airport_by_code_url(self):
        return self.config_reader.get('Airport', 'airport_by_code')

    @property
    def rapidapi_host_name(self):
        return self.config_reader.get('Airport', 'rapidapi_host_name')

    @property
    def rapidapi_airport_host_value(self):
        return self.config_reader.get('Airport', 'rapidapi_airport_host_value')

    @property
    def rapidapi_key_name(self):
        return self.config_reader.get('Airport', 'rapidapi_key_name')

    @property
    def rapidapi_key_value(self):
        return self.config_reader.get('Airport', 'rapidapi_key_value')

    @property
    def radius(self):
        return self.config_reader.get('Airport', 'radius')

    @property
    def get_quotes_url(self):
        return self.config_reader.get('Flight', 'get_quotes')

    @property
    def get_routes(self):
        return self.config_reader.get('Flight', 'get_routes')

    @property
    def rapidapi_flight_host_value(self):
        return self.config_reader.get('Flight', 'rapidapi_flight_host_value')

    @property
    def weather_url(self):
        return self.config_reader.get('Weather', 'weather_url')

    @property
    def weather_api_key(self):
        return self.config_reader.get('Weather', 'weather_api_key')

    @property
    def weather_api_value(self):
        return self.config_reader.get('Weather', 'weather_api_value')

    @property
    def units(self):
        return self.config_reader.get('Weather', 'units')

    @property
    def covid_url(self):
        return self.config_reader.get('Covid19', 'covid_url')

    @property
    def rapidapi_covid19_host_value(self):
        return self.config_reader.get('Covid19', 'rapidapi_covid19_host_value')


def http_request(url=None, headers=None, params=None):
    """Run a http request and return response"""
    try:
        response = requests.request("GET", url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.Timeout as e:
        print(f'Request timed out. Reason - {e}')
    except requests.exceptions.RequestException as e:
        print(f'Error while making request. Error - {e}')
