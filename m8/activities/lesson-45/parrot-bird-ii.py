class Parrot:
    name = "Polly"
    color = "green"
    age = 2

    def speak(self):
        print(self.name, "says: Hello!")

    def fly(self):
        print(self.name, "is flying!")

    def display(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Age:", self.age)

p1 = Parrot()
p1.display()
p1.speak()
p1.fly()

p2 = Parrot()
p2.name = "Tweety"
p2.color = "yellow"
p2.age = 1
p2.display()
p2.speak()
