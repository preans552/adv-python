class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching.")

class Admin(Person):
    def manage(self):
        print(f"{self.name} is managing school operations.")

s = Student("Alice", 14)
t = Teacher("Mr. Smith", 40)
a = Admin("Principal John", 50)

s.study()
t.teach()
a.manage()