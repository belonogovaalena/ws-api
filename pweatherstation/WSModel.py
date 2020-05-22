class WSModel:
    def __init__(self, altitude=None, luminosity=None, humidity=None, pressure=None, temperature=None, distance=None):
        self._altitude = altitude
        self._luminosity = luminosity
        self._humidity = humidity
        self._pressure = pressure
        self._temperature = temperature
        self._distance = distance

    @property
    def altitude(self) -> float:
        """
        :return: Высота точки измерения относительно места установки метеостанции, м
        """
        return self._altitude

    @altitude.setter
    def altitude(self, value: float):
        """
        :param value: Высота точки измерения относительно места установки метеостанции, м
        """
        self._altitude = value

    @property
    def luminosity(self) -> float:
        """
        :return: Уровень освещенности, люмен
        """
        return self._luminosity

    @luminosity.setter
    def luminosity(self, value: float):
        """
        :param value: Уровень освещенности, люмен
        """
        self._luminosity = value

    @property
    def humidity(self) -> float:
        """
        :return: Относительная влажность, %
        """
        return self._humidity

    @humidity.setter
    def humidity(self, value: float):
        """
        :param value: Относительная влажность, %
        """
        self._humidity = value

    @property
    def pressure(self) -> float:
        """
        :return: Давление, мм.рт.ст
        """
        return self._pressure

    @pressure.setter
    def pressure(self, value: float):
        """
        :param value: Давление, мм.рт.ст
        """
        self._pressure = value

    @property
    def temperature(self) -> float:
        """
        :return: Температура, *С
        """
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        """
        :param value: Температура, *С
        """
        self._temperature = value

    @property
    def distance(self):
        """
        :return: Расстрояние до ближайшего сотрудника, см
        """
        return self._distance

    @distance.setter
    def distance(self, value: float):
        """
        :param value: Расстрояние до ближайшего сотрудника, см
        """
        self._distance = value

    def is_empty(self) -> bool:
        """
        :return: Признак инициализации модели
        """
        return True if not self._distance and not self._temperature and not self._pressure and not self._altitude and \
            not self._luminosity and not self._distance else False
