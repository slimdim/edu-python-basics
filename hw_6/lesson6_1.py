# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    __color = ''

    def running(self, color):
        self.__color = color
        if self.__color == 'green':
            self.__timer_print(7)
        elif self.__color == 'yellow':
            self.__timer_print(3)
        elif self.__color == 'red':
            self.__timer_print(5)
        else:
            print(f'Color error for {self.__color}!')

    def __timer_print(self, seconds):
        i = 0
        while i < seconds:
            i += 1
            print(self.__color)
            sleep(1.0)


traffic_light = TrafficLight()
traffic_light.running('red')
traffic_light.running('yellow')
traffic_light.running('green')
traffic_light.running('purple')
