def circumference(radius):
    return 2 * 3.14159 * radius

r = float(input("Enter the radius: "))
result = circumference(r)
print("Circumference:", round(result, 2))
