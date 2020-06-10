# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс
# Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на
# реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


class Worker:
    name = ''
    surname = ''
    _income = dict()

    def set_income(self, wage, bonus):
        self._income.update({'wage': wage, 'bonus': bonus})

    def get_income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return ''.join(self.name + ' ' + self.surname)

    def get_total_income(self):
        income = self.get_income()
        return income.get('wage') + income.get('bonus')


position = Position()
position.name = 'Иван'
position.surname = 'Петров'
position.set_income(100000, 50000)
print(f'Имя: {position.name}')
print(f'Фамилия: {position.surname}')
print(f'Полное имя: {position.get_full_name()}')
print(f'Доход: {position.get_total_income()}')