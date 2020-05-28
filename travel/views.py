from django.shortcuts import render
from .forms import TravelForm
from utilities.scheduler import Scheduler


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
        results = s.dispatch(source=source, destination=destination,
                             country=country, travel_date=travel_date,
                             num_passengers=num_passengers)
        for k, v in results.items():
            data[k.__name__] = v
        # return render(request, 'results.html', {'data': data})
    return render(request, 'home.html', {'form': form,
                                         'Travel': data.get('Travel', None),
                                         'Weather': data.get('Weather', None)})
