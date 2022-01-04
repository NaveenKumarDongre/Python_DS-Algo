class Name:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name


class Student:
    def __init__(self, roll_no, s_name, course):
        self.roll_no = roll_no
        self.student_name = s_name
        self.course = course


student1 = Student(37, Name("Naveen", "Kumar", "Dongre"), "Python OOP")
student2 = Student(34, Name("Navin", "Kumar", "Dongre"), "JavaScript OOP")
student3 = Student(33, Name("Navo", "Kumar", "Dongre"), "C++ OOP")

students = [student1, student2, student3]

for student in students:
    print(f"Roll Number: {student.roll_no}\nStudent Name:{student.student_name.first_name} {student.student_name.middle_name} {student.student_name.last_name}\nCourse Name: {student.course}")
    print("  ")
