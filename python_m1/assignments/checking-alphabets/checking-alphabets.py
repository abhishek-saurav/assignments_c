letter = input("Enter a single alphabet: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(letter, "is a small vowel")
elif letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
    print(letter, "is a capital vowel")
else:
    print(letter, "is a consonant")

if letter >= "a" and letter <= "z":
    print("It is a small letter")
elif letter >= "A" and letter <= "Z":
    print("It is a capital letter")
else:
    print("It is not an alphabet")

if not (letter == " "):
    print("You did not enter a space")

if letter == "A" or letter == "a":
    print("This is the first letter of the alphabet")
