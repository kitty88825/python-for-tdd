from django.urls import reverse
from django.test import TestCase

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = reverse('/')
        self.assertEqual(found.func, home_page)
