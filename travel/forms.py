from django.forms import ModelForm

from .models import Travel


class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = ['source', 'destination', 'country', 'travel_date', 'num_passengers']
