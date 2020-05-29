import unittest
from WSService import WSService


class WSStructure(unittest.TestCase):
    def setUp(self):
        self.service = WSService()

    def test(self):
        # не доделано от группы. первая строчка, пришедшая от устройства 3, не валидна всегда
        self.service.get_model()
        model = self.service.get_model()
        self.assertIsNotNone(model.altitude)
        self.assertIsNotNone(model.luminosity)
        self.assertIsNotNone(model.temperature)
        self.assertIsNotNone(model.humidity)
        self.assertIsNotNone(model.pressure)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(WSStructure)
    unittest.TextTestRunner().run(suite)