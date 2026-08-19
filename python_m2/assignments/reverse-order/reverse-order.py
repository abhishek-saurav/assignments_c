num = int(input("Enter a number: "))

original = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print("")
print("===== REVERSE ORDER =====")
print("Name: Abhishek")
print("Original number:", original)
print("Reversed number:", reversed_num)
print("==========================")
