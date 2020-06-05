# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат
# вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def my_multiplication(x1, x2): return x1 * x2


start = 100
stop = 1000
step = 2
stop += step

my_list = [el for el in range(start, stop, step)]
print(f'Список:\n{my_list}')
print(f'Результат через lambda-функцию:\n{reduce((lambda x, y: x * y), my_list)}')
print(f'Результат через функцию:\n{reduce(my_multiplication, my_list)}')
