n = int(input("Enter a number: "))

single_value = n * 2
print("O(1) space: stored one value:", single_value)

numbers = []
for i in range(1, n + 1):
    numbers.append(i)
print("O(n) space: stored", len(numbers), "values:", numbers)

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(i * n + j)
    matrix.append(row)
print("O(n^2) space: stored", n * n, "values in a", n, "x", n, "grid")
for row in matrix:
    print(row)
