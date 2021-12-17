class Student:

    passing_percentage = 40

    def __init__(self, name, rollno):
        self.__name = name
        self.rollno = rollno

    def student_details(self):
        print(self.__name, self.rollno)

    def is_passed(self, percentage):
        if percentage >= self.passing_percentage:
            print("Student Passed")
        else:
            print("Student Failed")

    # below method is called as the class method
    @staticmethod
    def welcome_to_school():
        print("Hey!, Welcome to the School")


student1 = Student("Naveen", 54)
student1.__name = "Avinash"
print(student1.__name)

print(student1.__dict__)
(hasattr(student1, 'name'))
student1.student_details()
student1.is_passed(30)
Student.welcome_to_school()
