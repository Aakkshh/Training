class School:
    total_students = 0 

    def __init__(self, name, students):
        self.name = name
        self.students = students
        School.total_students += students 

    def enroll_students(self, number_of_students):
        self.students += number_of_students
        School.total_students += number_of_students

    def display_details(self):
        print(f"Name: \"{self.name}\", Students: {self.students}, Total Students: {School.total_students}")

school = School(name="Greenwood High", students=300)

school.enroll_students(50) 

school.display_details()  
