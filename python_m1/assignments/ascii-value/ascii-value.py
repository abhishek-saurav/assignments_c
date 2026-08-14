letter = input("Enter a character: ")

ascii_value = ord(letter)
print("The ASCII value of", letter, "is", ascii_value)

number = int(input("Enter an ASCII number: "))
character = chr(number)
print("The character for", number, "is", character)

print("ASCII of A is:", ord("A"))
print("ASCII of a is:", ord("a"))
print("Difference between a and A is:", ord("a") - ord("A"))

print("Is the ASCII value an int?", type(ascii_value) is int)
print("Is the ASCII value even?", ascii_value % 2 == 0)

print("ASCII in binary form:", bin(ascii_value))
print("ASCII shifted left by 1:", ascii_value << 1)
print("ASCII shifted right by 1:", ascii_value >> 1)
