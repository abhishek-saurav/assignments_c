n = int(input("Enter a number: "))

binary = bin(n)[2:]
reversed_binary = binary[::-1]
result = int(reversed_binary, 2)

print("Original number:", n)
print("Binary:", binary)
print("Reversed binary:", reversed_binary)
print("Reversed bits as decimal:", result)
