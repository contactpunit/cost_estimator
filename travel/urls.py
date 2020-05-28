from django.urls import path
from travel import views as travel_views

app_name = 'travel'
urlpatterns = [
    path('', travel_views.travel_detail, name='travel'),
]
