import unittest
from WSService import WSService


class WSTypesTest(unittest.TestCase):
    def setUp(self):
        self.service = WSService()

    def test(self):
        # не доделано от группы. первая строчка, пришедшая от устройства 3, не валидна всегда
        self.service.get_model()
        model = self.service.get_model()
        if model.distance is not None:
            self.assertIsInstance(model.distance, float)
        if model.pressure is not None:
            self.assertIsInstance(model.pressure, float)
        if model.humidity is not None:
            self.assertIsInstance(model.humidity, float)
        if model.temperature is not None:
            self.assertIsInstance(model.temperature, float)
        if model.luminosity is not None:
            self.assertIsInstance(model.luminosity, float)
        if model.altitude is not None:
            self.assertIsInstance(model.altitude, float)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(WSTypesTest)
    unittest.TextTestRunner().run(suite)