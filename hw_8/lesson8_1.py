# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self._date = date

    @staticmethod
    def validate_date(date):
        try:
            day = int(date[0: 2])
            month = int(date[3: 5])
            year = int(date[6:])
            if date[2] == '-' and date[5] == '-' and len(date) == 10 and \
                    1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 9999:
                return True
            else:
                print('Ошибка формата')
                return False
        except ValueError:
            print('Ошибка формата')
            return False

    @classmethod
    def integers_from_date(cls, date):
        if cls.validate_date(date):
            return [int(date[0: 2]), int(date[3: 5]), int(date[6:])]
        else:
            return None


print(Date.validate_date('67-12-2012'))
print(Date.integers_from_date('666-12-2012'))
