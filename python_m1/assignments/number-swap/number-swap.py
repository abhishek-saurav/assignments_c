a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swap: a =", a, "and b =", b)

temp = a
a = b
b = temp

print("After swap : a =", a, "and b =", b)

x = int(input("Enter the third number: "))
y = int(input("Enter the fourth number: "))

print("Before swap: x =", x, "and y =", y)

x = x + y
y = x - y
x = x - y

print("After swap : x =", x, "and y =", y)
