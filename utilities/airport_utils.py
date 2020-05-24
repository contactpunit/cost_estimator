from .utils import ConfigReaderMixin, http_request
from geopy.geocoders import Nominatim
from .travelExceptions import *


class AirportTracker(ConfigReaderMixin):
    """Class to return valid airport with latitude and longitude"""

    def __init__(self, place, country_code):
        self.place = place
        self.country_code = country_code
        self.place_type = None
        self.url = None
        self.params = None
        # try:
        #     getattr(self, 'get_quotes_url')
        #     print('I am called')
        # except AttributeError:
        #     self.read_config()
        self.headers = {self.rapidapi_host_name: self.rapidapi_airport_host_value,
                        self.rapidapi_key_name: self.rapidapi_key_value, 'Content-Type': 'application/json'}

    def get_airport_by_name(self):
        """Return airport if name is given instead of airport code.
        If no airport found it looks for nearest airport in radius of x kms"""

        self.place_type = 'name'
        self._set_url_params(place_type=self.place_type)
        response = http_request(url=self.url, headers=self.headers, params=self.params)
        if response:
            for record in response:
                if record['city'].lower() == self.place.lower() and record['countryCode'] == self.country_code:
                    return {'records': response}
            raise ValueError('Invalid place. Please enter correct value')
        else:
            lat, long = self.get_lat_long(place=self.place)
            response = self.get_airports_by_radius(lat=lat, long=long, radius=self.radius)
            return {'records': response, 'nearest': True}

    @staticmethod
    def get_lat_long(place=None):
        """ Return latitude longitude for a place based on name """

        geolocator = Nominatim(user_agent="Firefox")
        location = geolocator.geocode(place)
        if location:
            latitude, longitude = (location.latitude, location.longitude)
            return latitude, longitude
        else:
            raise LocationNotFoundException('Could not locate lat long for the place')

    def get_airport_by_code(self):
        """Returns airport based on airport code"""

        self.place_type = 'code'
        self._set_url_params(place_type=self.place_type)
        response = http_request(url=self.url, headers=self.headers, params=self.params)
        return {'records': response}

    def get_airports_by_radius(self, lat=None, long=None, radius=0):
        """Returns airports in radius of <radius> km. Input required latitude and longitude"""

        if lat is not None and long is not None:
            self._set_url_params(lat=lat, long=long, radius=radius)
            response = http_request(url=self.url, headers=self.headers, params=self.params)
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

    def __call__(self, *args, **kwargs):
        if len(self.place) == 3:
            return self.get_airport_by_code()
        elif len(self.place) > 3:
            return self.get_airport_by_name()
        else:
            raise InvalidCityException('Invalid place name. Please enter either code or full name')
