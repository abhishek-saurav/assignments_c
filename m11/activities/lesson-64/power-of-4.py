n = int(input("Enter a number: "))

if n > 0 and (n & (n - 1)) == 0:
    count = 0
    temp = n
    while temp > 1:
        temp = temp >> 1
        count = count + 1
    if count % 2 == 0:
        print(n, "is a power of 4")
    else:
        print(n, "is not a power of 4")
else:
    print(n, "is not a power of 4")
