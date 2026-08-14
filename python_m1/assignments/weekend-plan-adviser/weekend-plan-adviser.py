print("=== Weekend Plan Adviser ===")
print("Answer 3 quick questions and I will suggest a plan!\n")

day = input("Which day is it? (Monday to Sunday): ")
weather = input("What is the weather? (sunny / rainy / cloudy): ")
practice = input("Is your chess practice done? (yes / no): ")

print("")
print("=== Plan for Abhishek of St. Alberts ===")

if day == "Saturday" or day == "Sunday":
    print("Day type    : Weekend - plenty of free time!")
elif day == "Friday":
    print("Day type    : Last school day. Pack for the weekend.")
elif day == "Monday":
    print("Day type    : Fresh start to the week. Stay focused.")
elif day == "Tuesday" or day == "Wednesday" or day == "Thursday":
    print("Day type    : Regular school day.")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

if weather == "sunny" and practice == "yes":
    print("Suggestion  : Take the camera out for some photography.")

if weather == "rainy" or weather == "cloudy":
    print("Reminder    : Carry an umbrella today.")

if not (practice == "yes"):
    print("Chess       : Practice is still pending. Finish it first.")

if weather == "rainy" and not (practice == "yes"):
    print("Best plan   : Stay indoors, finish chess practice, then play the guitar.")
elif weather == "sunny" and practice == "yes" and not (day == "Saturday" or day == "Sunday"):
    print("Best plan   : School work first, then head outside with the camera.")
elif (day == "Saturday" or day == "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - photography and chess in the park!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print("")
print("Plan ready. Have a great day!")
