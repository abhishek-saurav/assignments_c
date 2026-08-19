connection = int(input("Enter 1 for Domestic, 2 for Commercial: "))

if connection == 1:
    units = int(input("Enter units consumed: "))
    if units <= 100:
        bill = units * 3
    else:
        bill = units * 5
    print("Domestic bill:", bill)
elif connection == 2:
    units = int(input("Enter units consumed: "))
    if units <= 100:
        bill = units * 6
    else:
        bill = units * 8
    print("Commercial bill:", bill)
else:
    print("That was not a valid choice.")
