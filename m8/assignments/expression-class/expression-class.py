class Expression:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"Expression created with {self.num1} and {self.num2}")

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("Cannot divide by zero!")
            return None

    def __del__(self):
        print("Expression object deleted.")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

expr = Expression(num1, num2)
print("Sum:", expr.add())
print("Difference:", expr.subtract())
print("Product:", expr.multiply())
print("Quotient:", expr.divide())
del expr
