num = int(input("Enter a decimal number: "))

original = num
binary = ""
if num == 0:
    binary = "0"
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("")
print("===== BINARY CONVERSION =====")
print("Name: Abhishek")
print("Decimal number:", original)
print("Binary number:", binary)
print("==============================")
