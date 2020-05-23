import logging
import os
import re
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from WSDriver import WSDriver
from WSModel import WSModel


class WSService:
    def __init__(self, speed='9600', export_log=False):
        self.logger = None
        if export_log:
            self.__init_logger()

        # инициализируем загрузку драйвера при подключении устройства
        self.driver = WSDriver()
        if self.driver.start_up(speed=speed) == 1:
            if self.logger is not None:
                self.logger.info("Connection to COM-port established")
        elif self.driver.start_up(speed=speed) == -1:
            if self.logger is not None:
                self.logger.info("Connection to COM-port not established")

        self._model = WSModel()

    def __init_logger(self):
        project_path = Path(__file__).parent.parent
        log_path = os.path.join(project_path, 'log')
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        self.logger = logging.getLogger('wsservice')

        log_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, 'wsservice.log'),
                                               when="midnight")
        log_formatter = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
        log_handler.setFormatter(log_formatter)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging.INFO)
        self.logger.info("WSService running...")

    def _sync(self):
        """
        Синхронизирует данные модели с данными от датчиков
        """
        self._model.clear()
        # все ошибки принтим
        line = self.driver.read_line()
        if not line:
            return -1
        else:
            if self.logger is not None:
                self.logger.info("Package recieved: {0} characters".format(len(line)))
        # определяем формат посылки

        # экземпляр № 1
        if re.match('LUM:[\d\.]* TMP:[\d\.]* PRS:[\d\.]* ATT:[\d\.]*', line):
            values = line.split(' ')
            try:
                self._model.luminosity = float(values[0].split(':')[-1])
                self._model.temperature = float(values[1].split(':')[-1])
                self._model.humidity = float(values[2].split(':')[-1])
                self._model.pressure = float(values[3].split(':')[-1])
                self._model.altitude = float(values[4].split(':')[-1])
                self._model.distance = None
                return 1
            except IndexError as e:
                print("Данные от датчиков представлены не в полном объеме")
                print(e)

        # экземпляр № 2
        elif 'Light' in line:
            self._model.luminosity = float(re.search('Light:(\d+) lux', line).group(1))
            temp_hum_line = self.driver.read_line()
            result = re.search('Temp:([-\d\.]+) °C Hum:([\d\.]+) %', temp_hum_line)
            self._model.temperature = float(result.group(1))
            self._model.humidity = float(result.group(2))
            dist_line = self.driver.read_line()
            self._model.distance = float(re.search('Dist:([\d\.]+) cm', dist_line).group(1))
            press_alt_line = self.driver.read_line()
            result = re.match('Pres:([\d\.]+) Att:([-\d\.]+)', press_alt_line)
            self._model.pressure = float(result.group(1))
            self._model.altitude = float(result.group(2))
            self.driver.read_line()
            return 1

        # экземпляр № 3
        elif 'Влажность' in line:
            self._model.humidity = float(re.search('Влажность:([\d\.]+)%', line).group(1))
            temp_line = self.driver.read_line()
            self._model.temperature = float(re.search('Температура:([-\d\.]+)°C', temp_line).group(1))
            # не доделано со стороны группы
            self.driver.read_line()
            lum_line = self.driver.read_line()
            self._model.luminosity = float(re.search('Свет:([-\d\.]+) lux', lum_line).group(1))
            press_line = self.driver.read_line()
            self._model.pressure = float(re.search('Давление:([-\d\.]+)мм.рт.ст.', press_line).group(1))
            alt_line = self.driver.read_line()
            self._model.altitude = float(re.search('Высота:([-\d\.]+)м.', alt_line).group(1))
            self.driver.read_line()
            return 1

        else:
            if len(line.split(' ')) > 0:
                if 'ERROR' in line.split(' ')[1]:
                    print(line)
            return -1

    def get_model(self):
        """
        :return: Модель с данными из датчиков
        """
        if self._sync() == 1 and self.logger is not None:
            self.logger.info("Parameters received")
        if not self._model.is_empty() and self.logger is not None:
            self.logger.info("Request to getting parameters. Model isn't empty")
        return self._model


if __name__ == '__main__':
    w = WSService(export_log=True)
    w.get_model()