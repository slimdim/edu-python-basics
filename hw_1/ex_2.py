# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

input_seconds = int(input('Введите время в секундах (целое число): '))
seconds = input_seconds % 60
minutes = input_seconds // 60 % 60
hours = input_seconds // 3600

print(f'Ваше время: {hours}:{minutes}:{seconds}')