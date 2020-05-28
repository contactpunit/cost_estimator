from django.shortcuts import render
from .forms import TravelForm
from utilities.scheduler import Scheduler


# Create your views here.
def travel_detail(request):
    data = {}
    form = TravelForm(request.POST or None)
    if form.is_valid():
        source = form.cleaned_data['source']
        destination = form.cleaned_data['destination']
        country = form.cleaned_data['country']
        travel_date = form.cleaned_data['travel_date']
        num_passengers = form.cleaned_data['num_passengers']
        s = Scheduler()
        results = s.dispatch(source=source, destination=destination, country=country, travel_date=travel_date,
                             num_passengers=num_passengers)
        for k, v in results.items():
            data[k.__name__] = v
        return render(request, 'results.html', {'data': data})
    return render(request, 'home.html', {'form': form})

# def itinerary(request):
#     form = TravelForm(request.POST or None)
#     if form.is_valid():
#         source = form.cleaned_data['source']
#         destination = form.cleaned_data['destination']
#         country = form.cleaned_data['country']
#         travel_date = form.cleaned_data['travel_date']
#         num_passengers = form.cleaned_data['num_passengers']
#         data = get_itinerary(source=source, destination=destination, country=country, travel_date=travel_date,
#                              num_passengers=num_passengers)
#         return render(request, 'results.html', {'data': data})
#         # return redirect('result/', {'data': data})
#
#     return render(request, 'home.html', {'form': form})


# def get_itinerary(source=None, destination=None, country=None, travel_date=None, num_passengers=0):
#     t = Travel(source=source, destination=destination, country=country, travel_date=travel_date,
#                num_passengers=num_passengers)
#     return t.find_itineraries()
