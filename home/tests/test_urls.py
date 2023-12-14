from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, plots

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_plots_url_is_resolved(self):
        url = reverse('plots')
        print(resolve(url))
        self.assertEquals(resolve(url).func, plots)