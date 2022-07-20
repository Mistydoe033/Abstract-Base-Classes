from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.Pi = 3.14
        self.diameter = self.radius * 2

    def area(self):
        return self.Pi * self.radius ** 2

    def perimeter(self):
        return self.diameter * self.Pi

class Triangle_90(Shape):
    def __init__(self, a, b):
        self.side1 = a
        self.side2 = b
        self.c2 = a**2 + b**2
        self.c = math.sqrt(self.c2)



    def area(self):
        return self.side1 * self.side2 / 2

    def perimeter(self):
        return self.side1 + self.side2 + self.c










square = Square(2)
print(square.area(),"Units**2")
print(square.perimeter(),"Units long") 

circle = Circle(15)
print(circle.area(),"Units**2")
print(circle.perimeter(),"Units long")

triangle = Triangle_90(130, 270)
print(triangle.area(),"Units**2")
print(triangle.perimeter(),"Units long")

