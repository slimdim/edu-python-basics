# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNum:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary > 0:
            return ''.join(f'{self.real} + {self.imaginary}i')
        elif self.imaginary == 0:
            return ''.join(f'{self.real}')
        else:
            return ''.join(f'{self.real} - {abs(self.imaginary)}i')

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNum(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.imaginary * other.imaginary,
                          self.real * other.imaginary + other.real * self.imaginary)


complex1 = ComplexNum(2, -2)
complex2 = ComplexNum(4, 8)
complex3 = ComplexNum(7, 0)

complex_sum = complex1 + complex2
complex_sub = complex3 - complex2
complex_mul = complex1 * complex2

print(complex1)
print(complex2)
print(complex3)
print(complex_sum)
print(complex_sub)
print(complex_mul)
