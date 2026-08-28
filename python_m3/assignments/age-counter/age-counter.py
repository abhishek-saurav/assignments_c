valid = False
while not valid:
    try:
        age = int(input("Enter your age: "))
        valid = True
    except ValueError:
        print("Invalid")

for year in range(1, age + 1):
    print("Year", year)
