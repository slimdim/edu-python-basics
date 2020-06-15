# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class OwnZeroDivision(ZeroDivisionError):
    def __init__(self, text):
        self._text = text


try:
    input_devisor = int(input('Введите делимое: '))
    input_devided = int(input('Введите делитель: '))
    if input_devided == 0:
        raise OwnZeroDivision('Деление на 0 невозможно')
except ValueError:
    print('Вы ввели не число')
except OwnZeroDivision as err:
    print(err)
else:
    print(f'Данные введены верно, результат деленя: {input_devisor / input_devided}')
