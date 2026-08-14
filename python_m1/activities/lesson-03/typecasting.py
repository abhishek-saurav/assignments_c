age = 31
age_text = str(age)
print("Age as text:", age_text, "-> type:", type(age_text))

marks_text = "88"
marks = int(marks_text)
print("Marks as a number:", marks, "-> type:", type(marks))

height_text = "1.72"
height = float(height_text)
print("Height as a decimal:", height, "-> type:", type(height))

score = 95.6
score_whole = int(score)
print("Score as a whole number:", score_whole, "-> type:", type(score_whole))

number = input("Enter a number: ")
print("The input is:", number, "-> type:", type(number))

number = int(number)
print("After typecasting:", number, "-> type:", type(number))
print("Double the number is:", number * 2)
