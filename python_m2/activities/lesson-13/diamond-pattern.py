rowSize = int(input("Enter row size: "))

if rowSize % 2 == 0:
    halfDiamRow = rowSize // 2
else:
    halfDiamRow = (rowSize // 2) + 1

space = halfDiamRow - 1
num = 1
for i in range(1, halfDiamRow + 1):
    for j in range(1, space + 1):
        print(" ", end="")
    space = space - 1
    for k in range(1, 2 * i):
        print(num, end="")
        num += 1
    print()

space = 1
for i in range(1, halfDiamRow):
    for j in range(1, space + 1):
        print(" ", end="")
    space = space + 1
    count = 2 * (halfDiamRow - i) - 1
    for k in range(count):
        print(num, end="")
        num += 1
    print()
