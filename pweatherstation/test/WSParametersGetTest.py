import unittest
from WSService import WSService


class WSParametersGetTest(unittest.TestCase):
    def setUp(self):
        self.service = WSService()

    def test(self):
        # не доделано от группы. первая строчка, пришедшая от устройства 3, не валидна всегда
        self.service._sync()
        self.assertIs(self.service._sync(), 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(WSParametersGetTest)
    unittest.TextTestRunner().run(suite)