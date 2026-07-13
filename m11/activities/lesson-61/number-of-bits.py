n = int(input("Enter a number: "))

count = 0
temp = n
while temp > 0:
    if temp & 1 == 1:
        count = count + 1
    temp = temp >> 1

print("Number of set bits (1s) in", n, "is", count)
