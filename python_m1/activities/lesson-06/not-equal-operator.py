a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a != b:
    print(a, "is not equal to", b)
else:
    print(a, "is equal to", b)

password = input("Enter the password: ")

if password != "codingal":
    print("Wrong password")
else:
    print("Access granted")

if not (a == b):
    print("The two numbers are different")
