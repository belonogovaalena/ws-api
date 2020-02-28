# Weather Station API

Предоставляет данные, полученные с датчиков давления, влажности, освещенности и термометра, установленные на домашней метеостанции.

Является программным интерфейсом между стендом и GUI.

### Использование

Weather Station API реализован на:

* **Python**
* **Java**


#### Использование с Python3 [pweatherstation]

Для работы с ws-api необходимо иметь версию интерпретатора Python>=3.6 и установить
* pip(>=10.0.1)
* pyserial(>=3.4)

##### Запуск


```
from pweatherstation.WSService import WSService
service = WSService()
model = service.get_model()
# вывод в консоль высоты измерения относительно высоты установки метеостанции
print(model.altitude)
# вывод в консоль температуры в помещении в *С
print(model.temperature)
# вывод в консоль давления в помещении в мм.рт.ст.
print(model.pressure)
# вывод в консоль относительной влажности в помещении в %
print(model.humidity)
# вывод в консоль степени освещенности помещения в люмен
print(model.luminosity)
```

#### Использование с Java8 [jweatherstation]

Для работы с ws-api необходимо иметь версию JDK>=8.0, интерпретатора Python>=3.6, а также установить значение параметра "python" в конфигурационном 
файле jweatherstation/resources/ws.properties путь к интерпретатору Python3.

* _Windows:_ C:\Python3X\python
* _osx|*unix:_ /usr/bin/python3

##### Запуск


```
WSService service = new WSService();
WSModel model = service.getModel();
// вывод в консоль высоты измерения относительно высоты установки метеостанции
System.out.println(model.getAltitude());
// вывод в консоль температуры в помещении в *С
System.out.println(model.getHumidity());
// вывод в консоль давления в помещении в мм.рт.ст.
System.out.println(model.getLuminosity());
// вывод в консоль относительной влажности в помещении в %
System.out.println(model.getPressure());
// вывод в консоль степени освещенности помещения в люмен
System.out.println(model.getTemperature());
```
