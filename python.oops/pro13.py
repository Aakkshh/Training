class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.__class__.__name__}: {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)


car = Car(make="Toyota", model="Camry")
bike = Bike(make="Yamaha", model="MT-07")

print(car)  
print(bike)