# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

input_number = int(input('Введите целое число: '))
result = input_number + input_number ** 2 + input_number ** 3

print(F'Рузультат операции n + nn + nnn: {result}')