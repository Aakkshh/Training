class Company:
    industry = "Technology"  # Class variable to represent the industry

    def __init__(self, name, num_employees):
        self.name = name
        self.num_employees = num_employees

    def update_employees(self, new_num_employees):
        self.num_employees = new_num_employees

    def display_details(self):
        print(f"Name: \"{self.name}\", Number of Employees: {self.num_employees}, Industry: {Company.industry}")


company = Company(name="TechCorp", num_employees=200)

company.update_employees(220)  

company.display_details()  
