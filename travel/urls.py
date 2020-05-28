from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [
    path('', views.travel_detail, name='travel'),
    # path(r'result/', views.details, name='details')
]
