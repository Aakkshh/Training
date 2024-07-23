class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee: {self.name}"

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def __str__(self):
        return f"Manager: {self.name}, Department: {self.department}"

class Engineer(Employee):
    def __init__(self, name, field):
        super().__init__(name)
        self.field = field

    def __str__(self):
        return f"Engineer: {self.name}, Field: {self.field}"

manager = Manager(name="John Doe", department="Sales")
engineer = Engineer(name="Jane Smith", field="Software")

print(manager)
print(engineer) 
