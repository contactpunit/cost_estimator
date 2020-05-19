import pytest
from manageflights.views import FlightTracker


def test_repr_of_class():
    f = FlightTracker('pnq', 'IN', 'del', 'IN', 2)
    assert repr(f) == '(FlightTracker) from pnq to del for 2 travellers'


def test_get_flight_from_source_to_destination():
    pass


def test_get_price_of_flight():
    pass


def get_flights_from_nearest_airport():
    pass
