from django.shortcuts import render


# Create your views here.
def get_itinerary(request):
    pass


def index(request):
    return render(request, 'home.html')
