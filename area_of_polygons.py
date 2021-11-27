class Polygon:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle(Polygon):
    def calculate_area(self):
        print(self.x * self.y / 2)


class Square(Polygon):

        
    def calculate_area(self):
        print(self.x * self.y)



trojkat = Triangle(1,2)
trojkat.calculate_area()

square = Square(1,2)
square.calculate_area()

