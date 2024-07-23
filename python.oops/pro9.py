import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"Square(side={self.side})"


circle = Circle(radius=4)
square = Square(side=5)

print(f"{circle} area: {circle.area()}, {circle} perimeter: {circle.perimeter()}")
print(f"{square} area: {square.area()}, {square} perimeter: {square.perimeter()}")
