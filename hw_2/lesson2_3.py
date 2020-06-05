# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

user_month = int(input('Введите номер месяца (от 1 до 12): '))
while user_month < 1 or user_month > 12:
    user_month = int(input('Кажется, вы указали неверный месяц, попробуйте ещё раз: '))

# Решение через list
seasons_list_num = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
seasons_list = ['зима', 'весна', 'лето', 'осень']
for index, season in enumerate(seasons_list_num):
    if user_month in season:
        print(seasons_list[index])

# Решение через dict
seasons_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for season_name, season in seasons_dict.items():
    if user_month in season:
        print(season_name)
