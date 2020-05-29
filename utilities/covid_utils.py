from utilities.utils import ConfigReaderMixin, http_request


class Covid(ConfigReaderMixin):
    def __init__(self, country=None, **kwargs):
        self.country = country
        self.params = {'country': self.country}
        self.headers = {self.rapidapi_host_name: self.rapidapi_covid19_host_value,
                        self.rapidapi_key_name: self.rapidapi_key_value,
                        'Content-Type': 'application/json'}

    def get_covid_details(self):
        url = self.covid_url
        response = http_request(url=url, params=self.params, headers=self.headers)
        return response
