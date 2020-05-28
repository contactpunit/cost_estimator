from utilities.utils import ConfigReaderMixin, http_request


class Weather(ConfigReaderMixin):
    def __init__(self, country=None, destination=None, **kwargs):
        self.country = country
        self.destination = destination
        self.params = {'units': self.units, 'q': ','.join([self.destination, self.country]),
                       self.weather_api_key: self.weather_api_value}
        self.headers = {'Content-Type': 'application/json'}

    def get_weather_details(self):
        url = self.weather_url
        response = http_request(url=url, params=self.params, headers=self.headers)
        return response

    def run(self):
        return self.get_weather_details()

# w = Weather(country='India', destination='Pune')
# w.get_weather_details()