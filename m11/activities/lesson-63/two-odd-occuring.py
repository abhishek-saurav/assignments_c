n = int(input("How many numbers? "))

numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

xor_all = 0
for num in numbers:
    xor_all = xor_all ^ num

rightmost_bit = xor_all & (-xor_all)

group1 = 0
group2 = 0
for num in numbers:
    if num & rightmost_bit != 0:
        group1 = group1 ^ num
    else:
        group2 = group2 ^ num

print("The two numbers occurring odd number of times are:", group1, "and", group2)
