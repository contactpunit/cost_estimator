import pytest
from utilities.utils import FlightTracker


# def test_repr_of_class():
#     f = FlightTracker(source='pnq', country='IN', destination='del', num_travellers=2)
#     assert repr(f) == '(FlightTracker) from pnq to del for 2 travellers'


# def test_get_flight_from_source_to_destination():
#     pass
#
#
# def test_get_price_of_flight():
#     pass
#
#
# def get_flights_from_nearest_airport():
#     pass

def test_check_quote_url():
    f = FlightTracker(source='pnq', country='IN', destination='del', num_travellers=2)
    assert f.get_quotes_url() == 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/'
