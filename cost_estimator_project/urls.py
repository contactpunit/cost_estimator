from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('costadmin/', admin.site.urls),
    path('', include('travel.urls')),
]
