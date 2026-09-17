class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Bird):
    def fly(self):
        super().fly()
        print("Wait, actually I cannot fly, I swim instead")

bird1 = Bird()
penguin1 = Penguin()

bird1.fly()
penguin1.fly()
