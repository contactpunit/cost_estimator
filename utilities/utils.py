# Create your views here.
import requests
import configparser
import os


class ConfigReaderMixin:
    def read_config(self):
        config_reader = configparser.ConfigParser()
        config_reader.read(os.path.join(os.path.dirname(__file__), 'conf.ini'))
        self.airport_by_radius_url = config_reader.get('Airport', 'airport_by_radius')
        self.airport_by_name_url = config_reader.get('Airport', 'airport_by_name')
        self.nearest_airport_url = config_reader.get('Airport', 'nearest_airport')
        self.airport_by_code_url = config_reader.get('Airport', 'airport_by_code')
        self.rapidapi_host_name = config_reader.get('Airport', 'rapidapi_host_name')
        self.rapidapi_airport_host_value = config_reader.get('Airport', 'rapidapi_airport_host_value')
        self.rapidapi_key_name = config_reader.get('Airport', 'rapidapi_key_name')
        self.rapidapi_key_value = config_reader.get('Airport', 'rapidapi_key_value')
        self.radius = config_reader.get('Airport', 'radius')
        self.get_quotes_url = config_reader.get('Flight', 'get_quotes')
        self.get_routes = config_reader.get('Flight', 'get_routes')
        self.rapidapi_flight_host_value = config_reader.get('Flight', 'rapidapi_flight_host_value')


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


