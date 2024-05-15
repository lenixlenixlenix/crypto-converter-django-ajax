from django.test import TestCase
from django.urls import reverse
import json

from .functions import CryptoClass

# Create your tests here.

class Tests(TestCase):
    def test_result_if_float_response(self):
        number = CryptoClass.convert_crypto(1, 2, 20)
        self.assertTrue(type(number) is float)

    def test_correct_url(self):
        url = reverse("home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Crypto currency converter", resp.content.decode())






