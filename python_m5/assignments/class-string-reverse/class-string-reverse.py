class StringReverser:
    def __init__(self, text):
        self.__text = text

    def reverse(self):
        return self.__text[::-1]

    def __str__(self):
        return f"Reversed: {self.reverse()}"

text = input("Enter a string: ")
reverser = StringReverser(text)
print(reverser)
