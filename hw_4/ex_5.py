# 5. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


from itertools import count, cycle

# Задание A
try:
    starting_num = int(input('Введите начальное число для генерации: '))
    end_num = int(input('Введите конечное число для генерации: '))
    for el in count(starting_num):
        if el > end_num:
            break
        else:
            print(el)
except ValueError:
    print('Ошибка ввода')

# Задание B
try:
    string_for_repeat = input('Введите строку для повтора: ')
    repeat_count = int(input('Укажите количество повторов символов: '))
    count = 0
    for el in cycle(string_for_repeat):
        if count >= repeat_count:
            break
        print(el)
        count += 1
except ValueError:
    print('Ошибка ввода')