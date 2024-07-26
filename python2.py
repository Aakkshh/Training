class student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
        print(f'{name},{age},{grades}')

r=student('ayush',23,[90,99,200])

print("-------------------------------------------------------------")

class bank:
    def __init__(self,acc,bal):
        self.acc=acc
        self.bal=bal
        print(f'{acc},{bal}')
s=bank(123344455,10000)

print("-------------------------------------------------------------")

class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(l,b):
        a=l*b
        print(a)
    def peri(l,b):
        p=2*(l+b)
        print(p)
    
rectangle.area(5,3)
rectangle.peri(5,3)

print("-------------------------------------------------------------")

class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        print(f"{self.make},{self.model},{self.year}")

car('toyota','camry',2024)

print("-------------------------------------------------------------")

class person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(f"name:{self.name},age:{self.age},add:{self.address}")
person('John',30,'1020 W')

print("-------------------------------------------------------------")

class circle:
    pi=3.14
    def __init__(self,r):
        self.r=r
    def area(r):
        a= (circle.pi)*(r*r)
        print(a)
    def peri(r):
        p=2*(circle.pi)*r
        print(p)
    
circle.area(4)
circle.peri(4)

print("-------------------------------------------------------------")

class Movie:
    def __init__(self,title,director,rating):
        self.title=title
        self.director=director
        self.rating=rating
        print(f"title: {self.title}, director: {self.director}, rating: {self.rating}")
Movie('inception','nolan',8)

print("-------------------------------------------------------------")


import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4*(self.length)

circle = Circle(5)
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

square = Square(4)
print(f"Square area: {square.area()}")
print(f"Square perimeter: {square.perimeter()}")

print("-------------------------------------------------------------")


class Employee:
    def __init__(self, name, department, field):
        self.name = name
        self.department = department
        self.field = field
    
    def display_info(self):
        return f"Name: {self.name}, Department: {self.department}, Field: {self.field}"

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name, department, "Management")
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Position: Manager"

class Engineer(Employee):
    def __init__(self, name, field):
        super().__init__(name, "Engineering", field)
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Position: Engineer"

manager = Manager("Alice Smith", "Sales")
print(manager.display_info())

engineer = Engineer("Bob Jones", "Software Development")
print(engineer.display_info())

print("-------------------------------------------------------------")

import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    def display_info(self):
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def display_info(self):
        return f"Circle - Radius: {self.radius}, " + super().display_info()

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display_info(self):
        return f"Rectangle - Width: {self.width}, Height: {self.height}, " + super().display_info()

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def display_info(self):
        return f"Square - Side Length: {self.width}, " + super().display_info()

circle = Circle(5)
print(circle.display_info())

rectangle = Rectangle(4, 6)
print(rectangle.display_info())

square = Square(4)
print(square.display_info())

print("-------------------------------------------------------------")


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"
    
    def vehicle_type(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Doors: {self.num_doors}, Type: Car"
    
    def vehicle_type(self):
        return "Car"

class Bike(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Type: Bike"
    
    def vehicle_type(self):
        return "Bike"

car = Car("Toyota", "Camry", 2020, 4)
print(car.display_info())

bike = Bike("Yamaha", "FZ-5", 2019)
print(bike.display_info())


print("-------------------------------------------------------------")

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book}" added to the library.')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'Book "{book}" removed from the library.')
        else:
            print(f'Book "{book}" not found in the library.')

    def display_info(self):
        return f"Name: {self.name}, Address: {self.address}, Books: {self.books}"

library = Library("City Library", "123 Main St")

library.add_book("Book1")
library.add_book("Book2")

library.remove_book("Book1")

print(library.display_info())

print("-------------------------------------------------------------")

class House:
    def __init__(self, address, num_rooms, price):
        self.address = address
        self.num_rooms = num_rooms
        self.price = price
    
    def display_details(self):
        return f"Address: {self.address}, Number of Rooms: {self.num_rooms}, Price: ${self.price:,.2f}"

house = House("456 Elm St", 4, 350000)

print(house.display_details())
print("-------------------------------------------------------------")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def discount(self, percentage):
        self.price -= self.price * percentage
        self.price = round(self.price, 2)  # Rounding to two decimal places

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}"

# Example usage:
book = Book("Python 101", "John Doe", 29.99)

# Applying discount
book.discount(0.1)

# Displaying book details
print(book.display_info())
print("-------------------------------------------------------------")

class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating
    
    def update_rating(self, new_rating):
        self.rating = new_rating

    def display_info(self):
        return f"Name: {self.name}, Cuisine Type: {self.cuisine_type}, Rating: {self.rating:.1f}"

# Example usage:
restaurant = Restaurant("Sushi Place", "Japanese", 4.5)

# Updating rating
restaurant.update_rating(4.8)

# Displaying restaurant details
print(restaurant.display_info())

print("-------------------------------------------------------------")

class School:
    total_students = 0 

    def __init__(self, name, students):
        self.name = name
        self.students = students
        School.total_students += students      
    def enroll_students(self, number):
        self.students += number
        School.total_students += number

    def display_info(self):
        return f"Name: {self.name}, Students: {self.students}, Total Students: {School.total_students}"

school = School("Greenwood High", 300)

school.enroll_students(50)

print(school.display_info())
print("-------------------------------------------------------------")

class Company:
    industry = "Technology"  

    def __init__(self, name, num_employees):
        self.name = name
        self.num_employees = num_employees
    
    def update_employees(self, new_count):
        self.num_employees = new_count

    def display_info(self):
        return f"Name: {self.name}, Number of Employees: {self.num_employees}, Industry: {Company.industry}"

company = Company("TechCorp", 200)

company.update_employees(220)

print(company.display_info())

print("-------------------------------------------------------------")

class MathUtils:
    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

print(MathUtils.is_prime(17))
print(MathUtils.is_prime(18)) 
print("-------------------------------------------------------------")

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))  
print("-------------------------------------------------------------")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Programming Language: {self.programming_language}"

developer = Developer("Alice", 70000, "Python")
print(developer.display_info())
print("-------------------------------------------------------------")

class Appliance:
    def turn_on(self):
        return "Appliance is turned on"

class WashingMachine(Appliance):
    def __init__(self, model):
        self.model = model
    
    def turn_on(self):
        return f"Washing Machine {self.model} is turned on"

appliance = Appliance()
washing_machine = WashingMachine("LG")

print(appliance.turn_on())
print(washing_machine.turn_on())
print("-------------------------------------------------------------")

class Pass:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def set_username(self, username):
        self.__username = username
    
    def set_password(self, password):
        self.__password = password

pwd = Pass("user1", "pass123")

print("Username:", pwd.get_username())
print("Password:", pwd.get_password())

pwd.set_password("newpass123")

print("Updated Password:", pwd.get_password())

print("-------------------------------------------------------------")

class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number

account = Account("987654321", 5000)
account.deposit(1500)
print("Balance after deposit:", account.get_balance())
account.withdraw(2000)
print("Balance after withdrawal:", account.get_balance())
print("Account Number:", account.get_account_number())
print("-------------------------------------------------------------")

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return f"{self.model} is driving"

class Bike(Vehicle):
    def move(self):
        return f"{self.model} is riding"

def operate_vehicle(vehicle):
    return vehicle.move()
car = Car("Toyota")
bike = Bike("Yamaha")

print(operate_vehicle(car))  
print(operate_vehicle(bike))  
print("-------------------------------------------------------------")

class Device:
    def __init__(self, model):
        self.model = model

    def operate(self):
        raise NotImplementedError("Subclasses must implement this method")

class Laptop(Device):
    def operate(self):
        return f"{self.model} is operating"

class Smartphone(Device):
    def operate(self):
        return f"{self.model} is operating"

def operate_device(device):
    return device.operate()

laptop = Laptop("Dell")
smartphone = Smartphone("iPhone")

print(operate_device(laptop))       
print(operate_device(smartphone))   

print("-------------------------------------------------------------")

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def travel(self):
        pass

class Bus(Transport):
    def __init__(self, route):
        self.route = route
    
    def travel(self):
        return f"Bus {self.route} is traveling"

class Train(Transport):
    def __init__(self, route):
        self.route = route
    
    def travel(self):
        return f"Train {self.route} is traveling"

bus = Bus("10A")
train = Train("Express")

print(bus.travel())  
print(train.travel()) 
print("-------------------------------------------------------------")

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self):
        pass

class CreditCard(Payment):
    def __init__(self, number):
        self.number = number
    
    def process(self):
        return f"Processing credit card payment for {self.number}"

class PayPal(Payment):
    def __init__(self, account):
        self.account = account
    
    def process(self):
        return f"Processing PayPal payment for {self.account}"

credit_card = CreditCard("1234")
paypal = PayPal("user@example.com")

print(credit_card.process())
print(paypal.process()) 
print("-------------------------------------------------------------")

