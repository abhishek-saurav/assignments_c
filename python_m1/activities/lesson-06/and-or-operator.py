age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

if age >= 18 and marks >= 40:
    print("You are eligible for the exam")

if age < 18 or marks < 40:
    print("You are not eligible for the exam")

weather = input("What is the weather? (sunny / rainy): ")
homework = input("Is your homework done? (yes / no): ")

if weather == "sunny" and homework == "yes":
    print("You can go out to play")
elif weather == "rainy" or homework == "no":
    print("Better to stay indoors")
else:
    print("Take your own decision")
