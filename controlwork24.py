from abc import ABC, abstractmethod
import math


class Shape(ABC):


    @abstractmethod
    def area(self):

        pass




class Rectangle(Shape):

    def init(self, width, height):
        self.width = width
        self.height = height


    def area(self):

        return self.width * self.height




class Circle(Shape):

    def init(self, radius):
        self.radius = radius


    def area(self):

        return math.pi * (self.radius ** 2)





rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area()) # Вывод: 50. (55 в примере использования - это, вероятно, опечатка, 10*5 = 50)
print(circle.area()) # Вывод: ~153.93... (7*7*pi ≈ 153.93, что соответствует ~150 из примера)

rect = Rectangle(10, 5)
circle = Circle(7)

print(f"Площадь прямоугольника (10x5): {rect.area()}")
print(f"Площадь круга (радиус 7): {circle.area():.2f}")