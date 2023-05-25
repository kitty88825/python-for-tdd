from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from app.lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self) -> None:
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self) -> None:
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
