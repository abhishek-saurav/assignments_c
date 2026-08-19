base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1
for i in range(exponent):
    result = result * base

print("")
print("===== POWER CALCULATOR =====")
print("Name: Abhishek")
print("Base:", base)
print("Exponent:", exponent)
print("Result:", result)
print("=============================")
