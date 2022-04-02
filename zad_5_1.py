class Rectangle:
    def __init__(self):
        print('Rectangle object created.')

    def read_data(self):
        self.a = float(input('Enter length of side a'))
        self.b = float(input('Enter length of side b'))

    def area(self):
        self.area = self.a * self.b
        return self.area

    def show(self):
        return self.a, self.b, self.area()


my_rectangle = Rectangle()
my_rectangle.read_data()




