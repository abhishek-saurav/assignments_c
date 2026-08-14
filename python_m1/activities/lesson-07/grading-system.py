mark1 = int(input("Enter marks in subject 1: "))
mark2 = int(input("Enter marks in subject 2: "))
mark3 = int(input("Enter marks in subject 3: "))
mark4 = int(input("Enter marks in subject 4: "))
mark5 = int(input("Enter marks in subject 5: "))

avg = (mark1 + mark2 + mark3 + mark4 + mark5) // 5
print("Average marks:", avg)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input!")
elif avg in range(91, 101):
    print("Grade: A+")
elif avg in range(81, 91):
    print("Grade: A")
elif avg in range(71, 81):
    print("Grade: B+")
elif avg in range(61, 71):
    print("Grade: B")
elif avg in range(51, 61):
    print("Grade: C+")
elif avg in range(41, 51):
    print("Grade: C")
elif avg in range(31, 41):
    print("Grade: D")
elif avg in range(21, 31):
    print("Grade: E")
elif avg in range(0, 21):
    print("Grade: F")
