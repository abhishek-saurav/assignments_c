n = int(input("Enter a number: "))
k = int(input("Enter bit position (0-indexed from right): "))

mask = 1 << k
result = n & mask

if result != 0:
    print("Bit at position", k, "in", n, "is SET (1)")
else:
    print("Bit at position", k, "in", n, "is NOT SET (0)")
