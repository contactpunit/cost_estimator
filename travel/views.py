from django.shortcuts import render, get_object_or_404, redirect
from .forms import TravelForm


# Create your views here.
def get_itinerary(request):
    pass


def itinerary(request):
    form = TravelForm(request.POST or None)
    if form.is_valid():
        return redirect('travel:results')
    return render(request, 'home.html', {'form': form})


def results(request):
    return render(request, 'answer.html')

# return render(request, 'home.html')
