import unittest
from WSService import WSService


class WSParametersSent(unittest.TestCase):
    def setUp(self):
        self.service = WSService()

    def test(self):
        # не доделано от группы. первая строчка, пришедшая от устройства 3, не валидна всегда
        self.service.get_model()
        self.assertIsNotNone(self.service.get_model())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(WSParametersSent)
    unittest.TextTestRunner().run(suite)