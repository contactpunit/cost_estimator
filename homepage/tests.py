from django.test import TestCase
from django.urls import resolve
from homepage.views import home_page
# Create your tests here.

class TestHomePage(TestCase):
    def test_root_url_resolution_o_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)