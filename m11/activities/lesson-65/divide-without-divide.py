a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

quotient = 0
dividend = a

while dividend >= b:
    dividend = dividend - b
    quotient = quotient + 1

print(a, "divided by", b, "=", quotient, "remainder", dividend)
