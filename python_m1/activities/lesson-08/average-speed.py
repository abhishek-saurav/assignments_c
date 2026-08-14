a = int(input("Enter the first speed: "))
b = int(input("Enter the second speed: "))
c = int(input("Enter the third speed: "))

avg = (a + b + c) / 3
print("Average speed:", avg)

if avg > a and avg > b and avg > c:
    print("higher than all three")
elif avg > a and avg > b:
    print("higher than a, b")
elif avg > b and avg > c:
    print("higher than b, c")
elif avg > a and avg > c:
    print("higher than a, c")
elif avg > a:
    print("just higher than a")
elif avg > b:
    print("just higher than b")
elif avg > c:
    print("just higher than c")
else:
    print("invalid input")
