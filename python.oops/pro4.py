class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Length: {self.length}, Width: {self.width}, Area: {self.area()}, Perimeter: {self.perimeter()}"

length = 5
width = 3
rectangle = Rectangle(length, width)

print(f"Area: {rectangle.area()}")        
print(f"Perimeter: {rectangle.perimeter()}")  
