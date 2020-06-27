# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.


class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self, max_capacity):
        self._max_capacity = max_capacity
        self._cur_capacity = max_capacity
        self._eq_dict = dict()

    def receive_eq(self, division, eq, count):
        if type(count) is int:
            if self._cur_capacity - count >= 0:
                temp_dict = self._eq_dict.get(division)
                if temp_dict is not None:
                    temp_dict.update({eq: count})
                else:
                    temp_dict = {eq: count}
                self._eq_dict.update({division: temp_dict})
                self._cur_capacity -= count
                print(f'Добавили в {division}: {eq.name} - {count} шт')
            else:
                print(f'Нет места для вашей оргтехники. Оставшееся количество единиц техники: {self._cur_capacity}')
        else:
            raise WarehouseError('Ошибка параметра count')

    def show_warehouse(self):
        for key, value in self._eq_dict.items():
            for key2, value2 in value.items():
                print(f'В {key} находится {key2.name} - {value2} шт')

    @property
    def cur_capacity(self):
        return self._cur_capacity


class Equipment:
    def __init__(self, name, type):
        self.name = name
        self._type = type


class Printer(Equipment):
    def __init__(self, name, is_colored):
        super().__init__(name, 'printer')
        self._is_colored = is_colored

    def printing(self):
        is_colored = 'цветной' if self._is_colored else 'ч/б'
        print(f'{self.name} печатает {is_colored}')


class Scanner(Equipment):
    def __init__(self, name, email_to_send):
        super().__init__(name, 'scanner')
        self._email_to_send = email_to_send

    def scanning(self):
        print(f'{self.name} сканирует и отправляет на {self._email_to_send}')


class Copier(Equipment):
    def __init__(self, name, format):
        super().__init__(name, 'copier')
        self._format = format

    def copying(self):
        print(f'{self.name} копирует формат {self._format}')


warehouse = Warehouse(10)
printer1 = Printer('HP', True)
printer1.printing()
printer2 = Printer('Canon', False)
printer2.printing()
scanner1 = Scanner('Brother', 'test@test.ru')
scanner1.scanning()
copier1 = Copier('Xerox', 'a4')
copier1.copying()

try:
    warehouse.receive_eq('бухгалтерия', printer1, 'ererer')
except WarehouseError as err:
    print(err)

warehouse.receive_eq('бухгалтерия', printer1, 2)
print(f'Осталось мест: {warehouse.cur_capacity}')
warehouse.receive_eq('бухгалтерия', printer2, 2)
print(f'Осталось мест: {warehouse.cur_capacity}')
warehouse.receive_eq('бухгалтерия', scanner1, 1)
print(f'Осталось мест: {warehouse.cur_capacity}')
warehouse.receive_eq('бухгалтерия', copier1, 1)
print(f'Осталось мест: {warehouse.cur_capacity}')
warehouse.receive_eq('столовая', printer1, 2)
print(f'Осталось мест: {warehouse.cur_capacity}')
warehouse.receive_eq('бухгалтерия', copier1, 1)
print(f'Осталось мест: {warehouse.cur_capacity}')
warehouse.receive_eq('столовая', copier1, 4)
warehouse.show_warehouse()
