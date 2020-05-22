from utilities import travel_utils
import pytest


@pytest.mark.parametrize('country_name, code', [
    ('india', 'IN'),
    ('United States of America', 'US'),
    ('spain', 'ES'),
    ('portugal', 'PT'),
    ('in', 'IN'),
])
def test_find_country_code(country_name, code):
    assert travel_utils.Travel.find_country_code(country_name) == code


@pytest.mark.parametrize('source, destination, country, travel_date', [
    ('PNQ', 'DEL', "INDIA", '2020-06-01')
])
@pytest.mark.skip
def test_find_itineraries(source, destination, country, travel_date):
    t = travel_utils.Travel(source=source, destination=destination, country=country, travel_date=travel_date,
                            num_passengers=2)
    assert 'CarrierName' in t.find_itineraries()
