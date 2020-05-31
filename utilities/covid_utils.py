from utilities.utils import ConfigReaderMixin, http_request
from .utils import find_country_name_from_code


class Covid(ConfigReaderMixin):
    def __init__(self, country=None, **kwargs):
        self.country = find_country_name_from_code(country.upper())
        self.params = {'country': self.country}
        self.headers = {self.rapidapi_host_name: self.rapidapi_covid19_host_value,
                        self.rapidapi_key_name: self.rapidapi_key_value,
                        'Content-Type': 'application/json'}

    def get_covid_details(self):
        url = self.covid_url
        response = http_request(url=url, params=self.params, headers=self.headers)
        return response

    def run(self):
        result = self.get_covid_details()
        return result

# c = Covid(country='in')
# print(c.run())
