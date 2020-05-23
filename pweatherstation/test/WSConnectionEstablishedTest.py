import unittest
from WSDriver import WSDriver


class WSConnectionEstablishedTest(unittest.TestCase):
    def setUp(self):
        self.driver = WSDriver()

    def test(self):
        self.assertTrue(True)
        self.assertIs(self.driver.start_up(), 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(WSConnectionEstablishedTest)
    unittest.TextTestRunner().run(suite)