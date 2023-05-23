from django.test import TestCase
from horoscope.views import zodiac

# Create your tests here.


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_page(self):
        for sign in zodiac:
            ru_name = zodiac[sign][1].split()[0]
            response = self.client.get(f'/horoscope/{sign}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(ru_name, response.content.decode())

    def test_page_redirect(self):
        for number, sign in enumerate(zodiac, 1):
            response = self.client.get(f'/horoscope/{number}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{sign}')
