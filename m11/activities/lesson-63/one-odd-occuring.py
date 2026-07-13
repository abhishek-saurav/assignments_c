n = int(input("How many numbers? "))

result = 0
for i in range(n):
    num = int(input("Enter number: "))
    result = result ^ num

print("The number occurring an odd number of times is:", result)
