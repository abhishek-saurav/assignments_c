numbers = [3, 7, 2, 9, 5, 1, 8, 4, 6, 10]

total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
print("Sum using index loop:", total)

total = 0
for num in numbers:
    total = total + num
print("Sum using for-each loop:", total)

print("Sum using built-in:", sum(numbers))
