# Weather Station API

Предоставляет данные, полученные с датчиков давления, влажности, освещенности и термометра, установленные на домашней метеостанции.

Является программным интерфейсом между стендом и GUI.

### Использование

Weather Station API реализован на:

* **Python**


#### Использование с Python3

Для работы с ws-api необходимо иметь версию интерпретатора Python>=3.6 и установить
* pip(>=10.0.1)
* pyserial(>=3.4)

##### Запуск


```
from pweatherstation.WSService import WSService
service = WSService()
# вывод в консоль высоты измерения относительно высоты установки метеостанции
print(service.get_model().altitude)
# вывод в консоль температуры в помещении в *С
print(service.get_model().temperature)
# вывод в консоль давления в помещении в мм.рт.ст.
print(service.get_model().pressure)
# вывод в консоль относительной влажности в помещении в %
print(service.get_model().humidity)
# вывод в консоль степени освещенности помещения в люмен
print(service.get_model().luminosity)
```
