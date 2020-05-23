# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# список параметров товара
params_list = ('название', 'цена', 'количество', 'eд')

# заполнение списка
my_goods_list = []
end_of_input = 'y'
index = 0
while end_of_input != 'n':
    my_goods_object = {}
    for param in params_list:
        goods_value = input(f'Введите значение параметра "{param}": ')
        if goods_value.isdigit():
            my_goods_object.update({param: int(goods_value)})
        else:
            my_goods_object.update({param: goods_value})
    index += 1
    my_goods_list.append((index, my_goods_object))
    end_of_input = input('Добавить ещё один товар (y/n)?\n')

print(f'Ваш список:\n{my_goods_list}')

# Тестовые данные для проверки сбора статистики (раскомментировать строчки ниже)
# my_goods_list = [(1, {'название': 'пк', 'цена': 20000, 'количество': 4, 'eд': 'шт'}),
#                 (2, {'название': 'принтер', 'цена': 8000, 'количество': 4, 'eд': 'шт'}),
#                 (3, {'название': 'сканер', 'цена': 5000, 'количество': 7, 'eд': 'шт'})]

# собираем статистику
my_goods_stat = {}
for param in params_list:
    stat_counter = set()
    for goods_object in my_goods_list:
        object_params = goods_object[1]
        stat_counter.add(object_params.get(param))
    my_goods_stat.update({param: list(stat_counter)})

print(f'\nСтатистика по товарам:\n{my_goods_stat}')
