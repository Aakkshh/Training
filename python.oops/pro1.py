class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f'name: "{self.name}", age: {self.age}, grades: {self.grades}'

student = Student(name="Alice", age=20, grades=[90, 85, 88])
print(student)
