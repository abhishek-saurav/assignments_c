maths = 88
science = 92
english = 79
hindi = 85
computer = 90

total = maths + science + english + hindi + computer
maximum = 500
percentage = total * 100 / maximum

print("Total marks obtained :", total)
print("Maximum marks        :", maximum)
print("Percentage           :", percentage)

print("Above 60 percent?    :", percentage > 60)
print("Above 90 percent?    :", percentage > 90)
print("Exactly 100 percent? :", percentage == 100)
