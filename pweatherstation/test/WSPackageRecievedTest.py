import unittest
from WSDriver import WSDriver


class WSPackageReceivedTest(unittest.TestCase):
    def setUp(self):
        self.driver = WSDriver()
        self.driver.start_up()

    def test(self):
        # не доделано от группы. первая строчка, пришедшая от устройства 3, не валидна всегда
        self.driver.read_line()
        self.assertIsNotNone(self.driver.read_line())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(WSPackageReceivedTest)
    unittest.TextTestRunner().run(suite)