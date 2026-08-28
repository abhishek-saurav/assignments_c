numbers = [4, 15, 8, 23, 42, 7, 16, 9]
print("Numbers:", numbers)

evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

big = [n for n in numbers if n > 10]
print("Numbers greater than 10:", big)

doubled = [n * 2 for n in numbers]
print("Doubled:", doubled)
