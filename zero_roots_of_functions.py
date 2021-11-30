import math


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show_equation(self):
        print('Something gone wrong')

class Linear(Equation):

    def show_equation(self):
        print(f'{self.a}+{self.b}x=0')

    def zeros(self):
        zero = - self.a / self.b
        return (f'Solution: x = {zero}')


class Quadratic(Equation):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def show_equation(self):
        print(f'{self.a}+{self.b}x+{self.c}x^2=0')

    def discriminant(self):
        delta = math.pow(self.b,2) - (4 * self.a * self.c)
        return delta

    def zeros(self):
        zero1 = (-(self.b) - math.sqrt(self.discriminant())) / (2 * self.c)
        zero2 = (-(self.b) + math.sqrt(self.discriminant())) / (2 * self.c)
        return (f'Solutions: x1 = {zero1}, x2 = {zero2}')


class Cubic(Equation):
    def __init__(self, a,b, c, d):
        super().__init__(a, b)
        self.c = c

    def show_equation(self):
        print(f'{self.a}+{self.b}x+{self.c}x^2+{self.d}^3=0')

    def zeros(self):
        pass
#
# linear = Linear(4,2)
# linear.show_equation()
# print(linear.zeros())

quadratic = Quadratic(-3,37,19)
quadratic.show_equation()
print(quadratic.discriminant())
print(quadratic.zeros())