import pytest
from utilities.airport_utils import AirportTracker
from utilities.travelExceptions import *


def test_no_argument_raise_keyerror():
    with pytest.raises(TypeError):
        a1 = AirportTracker()


def test_one_argument_raises_keyerror():
    with pytest.raises(TypeError):
        a1 = AirportTracker('pune')


def test_get_airport_by_name_url_used():
    a1 = AirportTracker('pune', 'IN')
    a1.get_airport_by_name()
    assert a1.url == 'https://cometari-airportsfinder-v1.p.rapidapi.com/api/airports/by-text'


def test_get_airport_by_code_url_used():
    a1 = AirportTracker('PNQ', 'IN')
    a1.get_airport_by_code()
    assert a1.url == 'https://cometari-airportsfinder-v1.p.rapidapi.com/api/airports/by-code'


def test_for_invalid_place_get_lan_long_raise_exception():
    a1 = AirportTracker('invalid', 'IN')
    with pytest.raises(LocationNotFoundException):
        a1.get_lat_long(place='invalidvalue')


@pytest.mark.parametrize('place, country', [
    ('PNQ', 'IN')
])
def test_get_lat_long_values(place, country):
    a1 = AirportTracker(place, country)
    assert a1.get_lat_long(place=place)[0] == pytest.approx(18.5804052)
    assert a1.get_lat_long(place=place)[1] == pytest.approx(73.91835)


@pytest.mark.parametrize('code, country', [
    ('PNQ', "IN")
])
def test_get_airport_by_code_valid_airport_listed_in_results(code, country):
    a1 = AirportTracker(code, country)
    assert a1.get_airport_by_code()['records'][0]['code'] == code


def test_get_airport_by_radius_for_city_without_airport():
    a1 = AirportTracker('latur', 'IN')
    assert a1.get_airport_by_name()['records'][0]['city'] == 'Nanded'
