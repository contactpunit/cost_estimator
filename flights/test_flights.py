import pytest
from utilities.flight_utils import FlightTracker


@pytest.fixture()
def return_flight_object():
    def flight_deco(**kwargs):
        return FlightTracker(source=kwargs['source'], country=kwargs['country'], travel_date='2020-06-01',
                             destination=kwargs['destination'],
                             num_travellers=2)

    return flight_deco


@pytest.mark.parametrize('source, destination, country ', [
    ('PNQ', 'DEL', 'IN')
])
def test_repr(return_flight_object, source, destination, country):
    f = return_flight_object
    result = f(source=source, destination=destination, country=country)
    assert repr(result) == f'(FlightTracker) from {source} to {destination}'


@pytest.mark.parametrize('source, destination, country', [
    ('NDC', 'DEL', 'IN')
])
def test_check_url(return_flight_object, source, destination, country):
    f = return_flight_object
    result = f(source=source, destination=destination, country=country)
    assert result.url == f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/' \
                         f'v1.0/{country}/INR/en-US/{source}/{destination}/2020-06-01'


def test_urls_read_from_conf(return_flight_object):
    f = return_flight_object
    result = f(source='DEL', destination='BOM', country='IN')
    print(result.get_quotes_url)
    assert result.get_quotes_url is not None


def test_get_flight_from_source_to_destination():
    source = 'PNQ'
    destination = 'DEL'
    country = 'IN'
    travel_date = '2020-06-01'
    f = FlightTracker(source=source, destination=destination, country=country, travel_date=travel_date)
    r = f.parse_results(f.get_flights())
    assert r.__class__.__name__ == 'dict'
    assert 'CarrierName' in r.keys()
