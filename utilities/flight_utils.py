from .utils import ConfigReaderMixin, http_request


class FlightTracker(ConfigReaderMixin):
    def __init__(self, source=None, country=None, destination=None, travel_date=None, num_travellers=0):
        self.source = source
        self.destination = destination
        self.country = country
        self.num_travellers = num_travellers
        self.travel_date = travel_date
        self.headers = {self.rapidapi_host_name: self.rapidapi_flight_host_value,
                        self.rapidapi_key_name: self.rapidapi_key_value, 'Content-Type': 'application/json'}
        self.url = self._prepare_url(source=self.source, destination=self.destination, country=self.country,
                                     travel_date=self.travel_date)
        self.params = {}

    def __repr__(self):
        return f'({self.__class__.__name__}) from {self.source} to {self.destination}'

    def _prepare_url(self, **kwargs):
        return self.get_quotes_url.format(source=kwargs['source'], destination=kwargs['destination'],
                                          country=kwargs['country'], travel_date=kwargs['travel_date'])

    def get_flights(self):
        response = http_request(url=self.url, params=self.params, headers=self.headers)
        return response

    def parse_results(self, response):
        if len(response['Quotes']) >= 1:
            price = response['Quotes'][0]['MinPrice']
            direct = True if response['Quotes'][0]['Direct'] else False
            carrier = response['Quotes'][0]['OutboundLeg']['CarrierIds'][0]
            for carriers in response['Carriers']:
                if carriers['CarrierId'] == carrier:
                    return {'MinPrice': price, 'CarrierName': carriers['Name'], 'direct': direct}

# f = FlightTracker(source='pnq', country='IN', destination='del', travel_date='2020-06-01', num_travellers=2)
# r = f.get_flights()
# print(f.parse_results(r))
