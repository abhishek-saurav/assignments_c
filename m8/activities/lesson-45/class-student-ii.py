class Student:
    name = "Aarav"
    age = 13
    grade = 7

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

    def greet(self):
        print("Hello! I am", self.name)

s1 = Student()
s1.display()
s1.greet()

s2 = Student()
s2.name = "Priya"
s2.age = 12
s2.grade = 6
s2.display()
