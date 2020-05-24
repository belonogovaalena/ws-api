import unittest
from WSService import WSService


class WSUpdateTest(unittest.TestCase):
    def setUp(self):
        self.service = WSService()

    def test(self):
        import copy
        # не доделано от группы. первая строчка, пришедшая от устройства 3, не валидна всегда
        self.service.get_model()
        self.service._sync()
        self.service._model.altitude = -9999
        model_1 = copy.copy(self.service._model)
        model_2 = self.service.get_model()
        flag = False
        if model_1.pressure != model_2.pressure:
            flag = True
        if model_1.humidity != model_2.humidity:
            flag = True
        if model_1.temperature != model_2.temperature:
            flag = True
        if model_1.luminosity != model_2.luminosity:
            flag = True
        if model_1.altitude != model_2.altitude:
            flag = True
        self.assertTrue(flag)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(WSUpdateTest)
    unittest.TextTestRunner().run(suite)