import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f'({self.x} , {self.y})'

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)

    def __gt__(self, other):
        return self.distancia() > other.distancia()


p1 = Punto(5, 8)
p2 = Punto(4, 9)
print(p1)
print(p1.distancia())
print(p2)
print(p2.distancia())
print(p1 > p2)
