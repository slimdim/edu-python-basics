# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.


russian_nums = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре', '5': 'Пять'}
with open('lesson5_4_eng.txt') as obj_f_eng:
    with open('lesson5_4_rus.txt', 'w') as obj_f_rus:
        for cur_string in obj_f_eng:
            my_list = cur_string.split()
            obj_f_rus.writelines(russian_nums.get(my_list[2]) + ' ' + my_list[1] + ' ' + my_list[2] + '\n')
