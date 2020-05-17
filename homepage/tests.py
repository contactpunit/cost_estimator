from django.test import TestCase
from django.urls import resolve
from homepage.views import home_page
from django.http import HttpRequest, HttpResponse
# Create your tests here.

class TestHomePage(TestCase):
    def test_root_url_resolution_o_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Cost Estimator</title>', html)
        self.assertTrue(html.endswith('</html>'))