roman_values = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
]

roman = input("Enter a Roman numeral: ").upper()
result = 0
i = 0
while i < len(roman):
    if i + 1 < len(roman):
        two = roman[i] + roman[i + 1]
        matched = False
        for symbol, value in roman_values:
            if two == symbol:
                result = result + value
                i = i + 2
                matched = True
                break
        if not matched:
            for symbol, value in roman_values:
                if roman[i] == symbol:
                    result = result + value
                    i = i + 1
                    break
    else:
        for symbol, value in roman_values:
            if roman[i] == symbol:
                result = result + value
                i = i + 1
                break

print(roman, "in decimal is", result)
