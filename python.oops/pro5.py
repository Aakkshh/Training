class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


make = "Toyota"
model = "Camry"
year = 2020
car = Car(make, model, year)

print(car) 