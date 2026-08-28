def sum_whole(n):
    if n == 0:
        return 0
    else:
        return n + sum_whole(n - 1)

number = int(input("Enter a number: "))
print("Sum of whole numbers up to", number, "is", sum_whole(number))
