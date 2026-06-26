class Parrot:
    name = "Polly"
    color = "green"

    def speak(self):
        print(self.name, "says: Hello!")

    def display(self):
        print("Name:", self.name)
        print("Color:", self.color)

p1 = Parrot()
p1.display()
p1.speak()
