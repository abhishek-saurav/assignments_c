weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

bmi = weight / (height * height)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")
