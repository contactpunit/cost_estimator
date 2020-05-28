from .travel_utils import Travel
from .weather_utils import Weather

REGISTERED = [Travel, Weather]


class Scheduler:
    def __init__(self):
        self.observers = dict()
        for app in REGISTERED:
            self.observers[app] = {}

    def dispatch(self, **kwargs):
        for app in self.observers.keys():
            s = app(**kwargs)
            self.observers[app] = s.run()
        return self.observers
