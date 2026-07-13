n = int(input("Enter a number: "))

if n <= 0:
    print(n, "is not a power of 8")
else:
    temp = n
    while temp % 8 == 0:
        temp = temp // 8
    if temp == 1:
        print(n, "is a power of 8")
    else:
        print(n, "is not a power of 8")
