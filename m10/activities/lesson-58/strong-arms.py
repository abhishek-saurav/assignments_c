n = int(input("Enter a number: "))

total = 0
i = 1
while i <= n:
    total = total + (i * i * i)
    i = i + 1

print("Sum of cubes from 1 to", n, "is", total)
