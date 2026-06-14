age = int(input("Enter your age: "))
marks = float(input("Enter your marks (out of 100): "))

if age >= 18:
    if marks >= 40:
        print("You are eligible for the exam")
    else:
        print("You are not eligible: Marks must be 40 or above")
else:
    print("You are not eligible: Age must be 18 or above")
