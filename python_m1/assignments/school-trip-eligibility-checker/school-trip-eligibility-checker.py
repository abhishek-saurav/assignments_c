age = int(input("Enter your age: "))

if age >= 18:
    permission = "not needed"
    print("You are an adult.")
    print("Parent permission is", permission)
else:
    permission = "needed"
    print("You are under 18.")
    print("Parent permission is", permission)

fee_paid = input("Has the trip fee been paid? (yes/no): ")

if fee_paid == "yes":
    print("Fee received. Thank you!")

distance = int(input("Enter the trip distance in km: "))

if distance > 100:
    stay = "overnight"
    print("This is a long trip.")
    print("Plan for an", stay, "stay")
else:
    stay = "same day"
    print("This is a short trip.")
    print("Plan for a", stay, "return")

lunch = input("Will you carry your own lunch? (yes/no): ")

if lunch == "yes":
    meal = "packed lunch"
    print("Remember to pack your lunch box.")
else:
    meal = "school lunch"
    print("A school lunch will be arranged.")

print("")
print("Trip check complete!")

print("===== SCHOOL TRIP CHECKLIST =====")
print("Name: Abhishek")
print("School: St. Alberts")
print("Age:", age)
print("Permission:", permission)
print("Fee Paid:", fee_paid)
print("Stay:", stay)
print("Meal:", meal)
print("=================================")
