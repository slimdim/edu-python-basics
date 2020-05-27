# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При
# нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод
# чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_sum(list_for_sum):
    result = 0
    for el in list_for_sum:
        result += el
    return result


result_sum = 0
while True:
    input_int = []
    input_string = input('Введите числовой ряд (n для выхода): ').split(' ')
    if 'n' in input_string:
        for el in input_string:
            if el == 'n':
                break
            else:
                input_int.append(int(el))
        result_sum += my_sum(input_int)
        print(result_sum)
        print(input_int)
        break
    for el in input_string:
        input_int.append(int(el))
    result_sum += my_sum(input_int)
    print(result_sum)
    print(input_int)
