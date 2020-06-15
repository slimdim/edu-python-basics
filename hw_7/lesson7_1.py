# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = 'Матрица:\n'
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result += f'{self.matrix[i][j]}    '
            result += '\n'
        return result

    def __add__(self, other):
        result = list()
        for i in range(len(self.matrix)):
            raw_result = list()
            for j in range(len(self.matrix[0])):
                raw_result.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(raw_result)
        return Matrix(result)


matrix1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix1)
print(matrix2)

my_result = matrix1 + matrix2
print(my_result)
