class RomanConverter:
    def __init__(self):
        self.values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    def to_roman(self, num):
        result = ""
        for i in range(len(self.values)):
            while num >= self.values[i]:
                result = result + self.symbols[i]
                num = num - self.values[i]
        return result

number = int(input("Enter a number: "))
converter = RomanConverter()
print("Roman numeral:", converter.to_roman(number))
