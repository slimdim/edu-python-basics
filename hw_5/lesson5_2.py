# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.


with open('lesson5_2.txt', 'r') as obj_f:
    strings_counter = 1
    words_counter = 0
    for cur_string in obj_f:
        words_in_cur_string = len(cur_string.split())
        print(f'В строке {strings_counter} количество слов {words_in_cur_string}')
        words_counter += words_in_cur_string
        strings_counter += 1

print(f'Всего строк в файле: {strings_counter}')
print(f'Всего слов в файле: {words_counter}')
