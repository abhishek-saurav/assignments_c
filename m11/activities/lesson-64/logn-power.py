n = int(input("Enter a number: "))
exp = int(input("Enter the exponent: "))

result = 1
base = n
while exp > 0:
    if exp & 1 == 1:
        result = result * base
    base = base * base
    exp = exp >> 1

print(n, "to the power", exp, "using log(n) steps")
print("Result:", result)
