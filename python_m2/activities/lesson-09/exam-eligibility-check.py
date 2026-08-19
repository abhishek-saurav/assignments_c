attendance = int(input("Enter your attendance percentage: "))

if attendance >= 75:
    marks = int(input("Enter your marks: "))
    if marks >= 40:
        print("You are eligible to sit for the exam")
    else:
        print("You are not eligible, your marks are too low")
else:
    print("You are not eligible, your attendance is too low")
