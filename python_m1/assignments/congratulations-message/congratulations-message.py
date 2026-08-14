name = input("Enter your name: ")
marks = input("Enter your marks: ")
total = input("Enter the total marks: ")

marks_number = int(marks)
total_number = int(total)
percentage = marks_number * 100 / total_number

print("Name:", name, "-> type:", type(name))
print("Marks:", marks_number, "-> type:", type(marks_number))
print("Percentage:", percentage, "-> type:", type(percentage))

percentage_text = str(percentage)
initial = name[0:1]

line_1 = "Congratulations " + name.upper() + "!"
line_2 = "You scored " + marks + " out of " + total
line_3 = "That is " + percentage_text + " percent"
line_4 = "Your initial is " + initial.upper()
line_5 = "From all of us at St. Alberts"

print("")
print("===== CONGRATULATIONS =====")
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print("===========================")
