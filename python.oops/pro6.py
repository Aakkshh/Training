class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


name = "John Doe"
age = 30
address = "123 Main St"
person = Person(name, age, address)

print(person)  
