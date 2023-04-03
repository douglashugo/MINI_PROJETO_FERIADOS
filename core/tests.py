from django.test import TestCase
from datetime import date

class NatalTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_natal_view_with_natal(self):
        request = self.factory.get('/')
        request.date = date(2023, 12, 25)
        response = natal(request)
        self.assertContains(response, 'É Natal')

    def test_natal_view_without_natal(self):
        request = self.factory.get('/')
        request.date = date(2023, 12, 24)
        response = natal(request)
        self.assertContains(response, 'Não é Natal')

class TiradentesTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_tiradentes_view_with_tiradentes(self):
        request = self.factory.get('/')
        request.date = date(2023, 4, 21)
        response = tiradentes(request)
        self.assertContains(response, 'É Tiradentes')

    def test_tiradentes_view_without_tiradentes(self):
        request = self.factory.get('/')
        request.date = date(2023, 4, 20)
        response = tiradentes(request)
        self.assertContains(response, 'Não é Tiradentes')