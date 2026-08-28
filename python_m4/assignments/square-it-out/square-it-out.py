numbers = [2, 5, 3, 8, 6, 1, 7]
print("Numbers:", numbers)

squares = []
for n in numbers:
    squares.append(n * n)
print("Squares:", squares)

print("First three squares:", squares[0:3])

squares.sort()
print("Sorted squares:", squares)

squares = squares[::-1]
print("Reversed squares:", squares)
