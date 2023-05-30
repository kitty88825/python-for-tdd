from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from app.lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self) -> None:
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self) -> None:
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
