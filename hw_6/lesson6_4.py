# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
#
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        if direction == 'left':
            print(f'{self.name} повернул налево')
        elif direction == 'right':
            print(f'{self.name} повернул налево')
        else:
            print('Неверное направление')

    def show_speed(self):
        print(f'Скорость равна: {self.speed}км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение! Скорость равна: {self.speed}км/ч')
        else:
            print(f'Скорость равна: {self.speed}км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение! Скорость равна: {self.speed}км/ч')
        else:
            print(f'Скорость равна: {self.speed}км/ч')


class PoliceCar(Car):
    pass


town_car = TownCar()
town_car.speed = 90
town_car.name = 'BMW'
town_car.color = 'Чёрный'
town_car.is_police = False
print(f'{town_car.color} {town_car.name} Полиция: {town_car.is_police} {town_car.speed}км/ч')
town_car.go()
town_car.turn('left')
town_car.turn('right')
town_car.turn('back')
town_car.stop()
town_car.show_speed()

print('**********************************************')

town_car.speed = 60
town_car.name = 'Opel'
town_car.color = 'Красный'
town_car.is_police = False
print(f'{town_car.color} {town_car.name} Полиция: {town_car.is_police} {town_car.speed}км/ч')
town_car.go()
town_car.turn('left')
town_car.turn('right')
town_car.turn('back')
town_car.stop()
town_car.show_speed()

print('**********************************************')

sport_car = SportCar()
sport_car.speed = 230
sport_car.name = 'Lamborghini'
sport_car.color = 'Минтовый'
sport_car.is_police = False
print(f'{sport_car.color} {sport_car.name} Полиция: {sport_car.is_police} {sport_car.speed}км/ч')
sport_car.go()
sport_car.turn('left')
sport_car.turn('right')
sport_car.turn('back')
sport_car.stop()
sport_car.show_speed()

print('**********************************************')

police_car = PoliceCar()
police_car.speed = 120
police_car.name = 'Ford'
police_car.color = 'Белый'
police_car.is_police = True
print(f'{police_car.color} {police_car.name} Полиция: {police_car.is_police} {police_car.speed}км/ч')
police_car.go()
police_car.turn('left')
police_car.turn('right')
police_car.turn('back')
police_car.stop()
police_car.show_speed()

print('**********************************************')

work_car = WorkCar()
work_car.speed = 50
work_car.name = 'Scania'
work_car.color = 'Оранжевый'
work_car.is_police = False
print(f'{work_car.color} {work_car.name} Полиция: {work_car.is_police} {work_car.speed}км/ч')
work_car.go()
work_car.turn('left')
work_car.turn('right')
work_car.turn('back')
work_car.stop()
work_car.show_speed()

print('**********************************************')

work_car.speed = 30
work_car.name = 'Газель'
work_car.color = 'Оранжевый'
work_car.is_police = False
print(f'{work_car.color} {work_car.name} Полиция: {work_car.is_police} {work_car.speed}км/ч')
work_car.go()
work_car.turn('left')
work_car.turn('right')
work_car.turn('back')
work_car.stop()
work_car.show_speed()
