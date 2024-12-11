class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

    def __str__(self):
        return f"Shape"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return round(0.5 * self.base * self.height, 2)

    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"


triangle = Triangle(base=5, height=3)
rectangle = Rectangle(length=4, width=2)

print(f"{triangle} area: {triangle.area()}")  
print(f"{rectangle} area: {rectangle.area()}")