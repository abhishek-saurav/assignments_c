n = int(input("Enter a number: "))

if n == 0:
    print("No set bits in 0")
else:
    position = 0
    temp = n
    while temp & 1 == 0:
        position = position + 1
        temp = temp >> 1

    print("First set bit (rightmost 1) in", n, "is at position", position, "(0-indexed from right)")
