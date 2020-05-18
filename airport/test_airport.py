import pytest
from airport.views import AirportTracker


def test_no_argument_raise_error():
    with pytest.raises(Exception):
        a1 = AirportTracker()
