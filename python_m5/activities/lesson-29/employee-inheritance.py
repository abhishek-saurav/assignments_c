class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print("Team size:", self.team_size)

emp1 = Employee("Abhishek", 40000)
mgr1 = Manager("Ravi", 80000, 6)

emp1.show_details()
mgr1.show_details()
