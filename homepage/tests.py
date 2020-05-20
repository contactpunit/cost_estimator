from django.test import TestCase
from django.urls import resolve
from homepage.views import home_page
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string


# Create your tests here.

class TestHomePage(TestCase):

    def test_uses_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
