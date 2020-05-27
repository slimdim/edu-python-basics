# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_data(user_name, user_surname, user_date_of_birth, user_city, user_email, user_phone):
    print(f'Имя: {user_name}, Фамилия: {user_surname}, Дата рождения: {user_date_of_birth}, '
          f'Город: {user_city}, Email: {user_email}, Телефон: {user_phone}')


user_data(user_date_of_birth='14.04.1992', user_city='Москва', user_phone='+7 (926) 111-22-33',
          user_email='test@python.com', user_name='Жора', user_surname='Петров')
