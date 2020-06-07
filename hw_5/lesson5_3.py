# Создать текстовый файл(не программно), построчно записать фамилии сотрудников и величину
# их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии
# этих сотрудников.Выполнить подсчет средней величины дохода сотрудников.


comparision_salary = 20000
salary_sum = 0
people_count = 0
with open('lesson5_3.txt', 'r') as obj_f:
    for cur_string in obj_f:
        my_list = cur_string.split()
        if int(my_list[1]) >= comparision_salary:
            print(f'У {my_list[0]} зарплата равна {my_list[1]} руб., что больше {comparision_salary}')
        salary_sum += int(my_list[1])
        people_count += 1

print(f'Средняя зарплата равна {salary_sum / people_count} руб.')
