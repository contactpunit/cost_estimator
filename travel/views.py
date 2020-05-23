from django.shortcuts import render, get_object_or_404
from .forms import TravelForm
from utilities.travel_utils import Travel



# Create your views here.

def itinerary(request):
    form = TravelForm(request.POST or None)
    if form.is_valid():
        source = form.cleaned_data['source']
        destination = form.cleaned_data['destination']
        country = form.cleaned_data['country']
        travel_date = form.cleaned_data['travel_date']
        data = get_itinerary(source=source, destination=destination, country=country, travel_date=travel_date)
        return render(request, 'results.html', {'data': data})
    return render(request, 'home.html', {'form': form})


def get_itinerary(source=None, destination=None, country=None, travel_date=None):
    t = Travel(source=source, destination=destination, country=country, travel_date=travel_date, num_passengers=1)
    return t.find_itineraries()

