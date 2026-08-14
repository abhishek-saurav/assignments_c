number = int(input("Enter a number: "))

square = number * number
square_root = number ** 0.5
half = number / 2
whole_root = int(square_root)

print("Number            :", number)
print("Square            :", square)
print("Square root       :", square_root)
print("Half the number   :", half)
print("Root as a whole   :", whole_root)

print("Is the root a whole number? :", square_root == whole_root)
print("Is the number bigger than 100? :", number > 100)
