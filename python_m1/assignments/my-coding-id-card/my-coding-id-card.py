import keyword

name = "Abhishek"
age = 31
school = "St. Alberts"
hobby = "chess"

print("===== MY CODING ID CARD =====")
print("Name:", name)
print("Age:", age)
print("School:", school)
print("Favourite hobby:", hobby)
print("Other hobbies:", "photography", "guitar", "coding")

print("\nCard printed successfully \n")

print("Card number: ", end="7")
print()

user_name = input("\nEnter your name: ")
print("\nHello", user_name, "\nwelcome to codingal")

print("\nPython reserved words are...\n")
print(keyword.kwlist)
