n = int(input("Enter the table size: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="  ")
    print()

mid = (n + 1) // 2
product = 1
for j in range(1, n + 1):
    product = product * (mid * j)

print(f"The product of the middle row (row {mid}) is {product}")
