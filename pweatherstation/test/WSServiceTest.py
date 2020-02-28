import unittest
from WSService import WSService


class WSServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = WSService()

    def test_nullable(self):
        """
        Тест, что данные от датчиков получены
        """
        self.assertIsNotNone(self.service.get_model().altitude)
        self.assertIsNotNone(self.service.get_model().humidity)
        self.assertIsNotNone(self.service.get_model().luminosity)
        self.assertIsNotNone(self.service.get_model().pressure)
        self.assertIsNotNone(self.service.get_model().temperature)

    def test_types(self):
        self.assertIsInstance(self.service.get_model().altitude, float)
        self.assertIsInstance(self.service.get_model().humidity, float)
        self.assertIsInstance(self.service.get_model().luminosity, float)
        self.assertIsInstance(self.service.get_model().pressure, float)
        self.assertIsInstance(self.service.get_model().temperature, float)
