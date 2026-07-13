n = int(input("Enter a number: "))

binary = bin(n)[2:]
ones = binary.count("1")
zeros = binary.count("0")

print("Binary of", n, "is:", binary)
print("Number of 1s:", ones)
print("Number of 0s:", zeros)
