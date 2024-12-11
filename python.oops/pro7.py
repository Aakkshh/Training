import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)

    def __str__(self):
        return f"Radius: {self.radius}, Area: {self.area()}, Circumference: {self.circumference()}"


radius = 4
circle = Circle(radius)

print(f"Area: {circle.area()}")           
print(f"Circumference: {circle.circumference()}")