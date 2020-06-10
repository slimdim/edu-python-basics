# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
# Рассчёт прибылей, средней прибыли и формирование результирующего списка
dict_profit = dict()
list_profit = list()
result_list = [dict_profit]

with open('lesson5_7.txt') as obj_f:
    for cur_string in obj_f:
        firm_list = cur_string.split()
        profit = int(firm_list[2]) - int(firm_list[3])
        dict_profit.update({firm_list[0]: profit})
        if profit >= 0:
            list_profit.append(profit)

result_list.append({'average_profit': sum(list_profit) / len(list_profit)})
print(result_list)

# Запись результатов в JSON
with open('lesson5_7.json', 'w') as json_f:
    json.dump(result_list, json_f)