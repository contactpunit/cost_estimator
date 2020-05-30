from utilities import covid_utils
import pytest


@pytest.mark.parametrize('country', [
    'india',
    'china',
    'usa'
])
def test_covid_returns_results_for_countries(country):
    c = covid_utils.Covid(country=country)
    assert c.get_covid_details().get('results') > 0


@pytest.mark.parametrize('country', [
    'invalid1',
    'invalid2',
])
def test_covid_return_zero_results_for_countries(country):
    c = covid_utils.Covid(country=country)
    assert c.get_covid_details().get('results') == 0


def test_covid_run_function():
    c = covid_utils.Covid('india')
    assert c.get_covid_details().get('results') > 0
