class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'Employee(name="{self.name}", position="{self.position}", salary={self.salary})'

    @staticmethod
    def from_list(data):
        employees = []
        for row in data:
            name, position, salary = row
            employees.append(Employee(name, position, salary))
        return employees

csv_content = [
    ["John Doe", "Manager", 75000],
    ["Jane Smith", "Engineer", 80000]
]

employees = Employee.from_list(csv_content)
for emp in employees:
    print(emp)
