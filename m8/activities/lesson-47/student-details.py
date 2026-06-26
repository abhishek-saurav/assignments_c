class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}  |  Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}  |  Grade: {self.grade}")

s1 = Student("Rahul", 13, "S001", 7)
s1.display()

print()

s2 = Student("Sneha", 12, "S002", 6)
s2.display()
