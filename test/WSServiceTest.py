import unittest
from pweatherstation.WSService import WSService


class WSServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = WSService()

    def test_nullable(self):
        """
        Тест, что данные от датчиков получены
        """
        self.assertIsNotNone(self.service.get_altitude())
        self.assertIsNotNone(self.service.get_humidity())
        self.assertIsNotNone(self.service.get_luminosity())
        self.assertIsNotNone(self.service.get_pressure())
        self.assertIsNotNone(self.service.get_temperature())

    def test_types(self):
        self.assertIsInstance(self.service.get_altitude(), float)
        self.assertIsInstance(self.service.get_humidity(), float)
        self.assertIsInstance(self.service.get_luminosity(), float)
        self.assertIsInstance(self.service.get_pressure(), float)
        self.assertIsInstance(self.service.get_temperature(), float)
