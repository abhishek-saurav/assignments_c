name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 5:
    if age <= 12:
        category = "Child ticket"
    else:
        if age <= 17:
            category = "Teen ticket"
        else:
            category = "Adult ticket"
else:
    category = "Not allowed"

print("")
print("===== TICKET CHECK =====")
print("Name:", name)
print("Age:", age)
print("Category:", category)
print("=========================")
