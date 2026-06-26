class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}  |  Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}  |  Department: {self.department}")

e1 = Employee("Aarav", 30, "E001", "Python Development")
e1.display()

print()

e2 = Employee("Priya", 28, "E002", "Data Science")
e2.display()
