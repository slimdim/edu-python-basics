# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(num_1, num_2, num_3):
    try:
        list_sorted = [int(num_1), int(num_2), int(num_3)]
        max_num_1 = max(list_sorted)
        list_sorted.remove(max_num_1)
        max_num_2 = max(list_sorted)
        return max_num_1 + max_num_2
    except ValueError:
        return


print(my_func(4, 1, 10))
print(my_func(4, 10, 1))
print(my_func(1, 4, 10))
print(my_func(1, 'none', 10))
