import driver
from .WSModel import WSModel


class WSService:
    def __init__(self):
        # инициализируем загрузку драйвера при подключении устройства
        driver.startup()
        self._model = WSModel()

    def _sync(self):
        """
        Синхронизирует данные модели с данными от датчиков
        """
        # загружаем данные от датчика в список
        # элементы списка соответствуют шаблону "КодПараметра:ЗначениеПараметра"
        values = driver.read_line().split(' ')
        # заполняем модель полученными данными
        try:
            self._model.luminosity = float(values[0].split(':')[-1])
            self._model.temperature = float(values[1].split(':')[-1])
            self._model.humidity = float(values[2].split(':')[-1])
            self._model.pressure = float(values[3].split(':')[-1])
            self._model.altitude = float(values[4].split(':')[-1])
        except IndexError as e:
            print("Данные от датчиков представлены не в полном объеме")
            print(e)

    def get_temperature(self) -> float:
        """
        :return: Температура воздуха в помещении, *С
        """
        self._sync()
        return self._model.temperature

    def get_pressure(self) -> float:
        """
        :return: Давление в помещении, мм.рт.ст
        """
        self._sync()
        return self._model.pressure

    def get_humidity(self) -> float:
        """
        :return: Относительная влажность в помещении, %
        """
        self._sync()
        return self._model.humidity

    def get_luminosity(self) -> float:
        """
        :return: Степень освещенности помещения, люмен
        """
        self._sync()
        return self._model.luminosity

    def get_altitude(self):
        """
        :return: Высота точки измерения относительно места установки метеостанции, м
        """
        self._sync()
        return self._model.altitude
