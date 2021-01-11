from django.test import TestCase

# Create your tests here.
from . import models

class TestURLs(TestCase):
    def test_math(self):
        self.assertEqual(1+1, 2)
