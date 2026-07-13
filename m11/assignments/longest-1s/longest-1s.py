n = int(input("Enter a number: "))

binary = bin(n)[2:]

max_len = 0
current = 0
for bit in binary:
    if bit == "1":
        current = current + 1
        if current > max_len:
            max_len = current
    else:
        current = 0

print("Binary of", n, ":", binary)
print("Longest sequence of 1s:", max_len)
