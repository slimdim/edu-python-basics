# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

integer_var = 25
float_var = 46.7
string_var = 'this is a string'
bool_var = True

print(f'integer: {integer_var}')
print(f'float: {float_var}')
print(f'string: {string_var}')
print(f'bool: {bool_var}')
print(f'**************')

integer_var = int(input('Введите целое число: '))
float_var = float(input('Введите дроюное число: '))
string_var = input('Введите строку: ')

print(f'integer: {integer_var}')
print(f'float: {float_var}')
print(f'string: {string_var}')