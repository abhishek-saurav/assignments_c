a = int(input("Enter the Maths score: "))
b = int(input("Enter the Science score: "))
c = int(input("Enter the English score: "))

avg = (a + b + c) / 3
print("Average score:", avg)

if avg > a and avg > b and avg > c:
    print("The average is higher than all three")
elif avg > a and avg > b:
    print("The average is higher than Maths, Science")
elif avg > b and avg > c:
    print("The average is higher than Science, English")
elif avg > a and avg > c:
    print("The average is higher than Maths, English")
elif avg > a:
    print("The average is just higher than Maths")
elif avg > b:
    print("The average is just higher than Science")
elif avg > c:
    print("The average is just higher than English")
else:
    print("invalid input")

total = a + b + c
print("Total score:", total)

if total % 3 == 0:
    print(str(total) + " is divisible by 3")
else:
    print(str(total) + " is not divisible by 3")

mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40

old_sum = mean1 * total_number
print("Original class total :", old_sum)

new_sum = old_sum - ((wrong_number) - (correct_number))
print("Corrected class total:", new_sum)

mean2 = new_sum / total_number
print("Corrected class mean :", mean2)

v = 4
w = 5
x = 8
y = 2

z = (v + w) * x / y
print("Value of (v+w) * x / y is", z)

name = "Abhishek"
age = 31

if name == "Abhishek" or name == "John" and age >= 2:
    print("Hello! Welcome to St. Alberts.")
else:
    print("Good Bye!!")
