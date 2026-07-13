name = "Sam"
age = 15
school = "Greenfield High School"

score = int(input("Enter " + name + "'s quiz score: "))

if score == 3000:
    print("Love you 3000,", name, "! Perfect score!")
elif score >= 2000:
    print("Love you", score, ",", name, "! Great job!")
elif score >= 1000:
    print(name, "scored", score, ". Keep going!")
else:
    print(name, "scored", score, ". Practice more!")

total = 0
i = 1
while i <= score:
    total = total + i
    i = i + 1
print("Sum from 1 to", score, "is", total)
