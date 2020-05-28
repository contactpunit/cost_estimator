from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from travel import urls as travel_urls

urlpatterns = [
    path('costadmin/', admin.site.urls),
    path('', include(travel_urls)),
]
