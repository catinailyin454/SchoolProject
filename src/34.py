class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, subject):
        print(f"{self.name} is studying {subject}")

student1 = Student("John", 16)
student2 = Student("Jane", 18)

student1.study("Math")
student2.study("Science")

# More methods and attributes can be added here
