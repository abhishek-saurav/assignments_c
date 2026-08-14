month = input("Enter the month name: ")

if month == "April":
    print("April is a summer month")
else:
    print("This may not be a summer month")

temperature = int(input("Enter today's temperature in Celsius: "))

if temperature > 35:
    advice = "stay indoors"
    print("It is very hot outside")
    print("Please", advice, "and drink plenty of water")
else:
    advice = "go outside"
    print("The weather is comfortable")
    print("You can", advice, "and play")

if temperature > 40:
    print("Heat wave warning!")

drink = input("Have you had water in the last hour? (yes/no): ")

if drink == "no":
    print("Go and drink a glass of water now")

print("")
print("===== SUMMER TIMES =====")
print("Name: Abhishek")
print("School: St. Alberts")
print("Month:", month)
print("Temperature:", temperature)
print("Advice:", advice)
print("========================")
