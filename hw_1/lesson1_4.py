# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

input_number = int(input('Введите целое положительное число: '))
max_number = 0

while input_number > 0:
    if input_number % 10 > max_number:
        max_number = input_number % 10
    input_number = input_number // 10

print(f'Максимальная цифра: {max_number}')