binary = input("Enter a binary number: ")

decimal = 0
power = 0
i = len(binary) - 1
while i >= 0:
    if binary[i] == "1":
        decimal = decimal + (2 ** power)
    power = power + 1
    i = i - 1

print("Binary", binary, "is", decimal, "in decimal")
