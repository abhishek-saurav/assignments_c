class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def __del__(self):
        print("Circle object destroyed")

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Name: Abhishek")
print("Radius:", circle.radius)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
