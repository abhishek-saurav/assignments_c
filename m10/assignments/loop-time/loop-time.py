n = int(input("Enter n: "))

print("O(1) block runs 1 time")
result = n * n
print("Square of", n, "is", result)

print("O(n) block runs", n, "times")
for i in range(1, n + 1):
    print("Step", i)

print("O(n^2) block runs", n * n, "times")
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        count = count + 1
print("Total iterations in nested loop:", count)
