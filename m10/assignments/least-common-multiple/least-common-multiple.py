a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b
while y != 0:
    remainder = x % y
    x = y
    y = remainder
gcd = x

lcm = (a * b) // gcd
print("LCM of", a, "and", b, "is", lcm)
