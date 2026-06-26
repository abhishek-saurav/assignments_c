class Robot:
    name = "Robo"
    model = "X100"
    battery = 100

    def introduce(self):
        print("Hi! I am", self.name)
        print("Model:", self.model)
        print("Battery:", self.battery, "%")

    def greet(self, user_name):
        print("Hello,", user_name, "! Nice to meet you.")

r1 = Robot()
r1.introduce()
user = input("Enter your name: ")
r1.greet(user)
