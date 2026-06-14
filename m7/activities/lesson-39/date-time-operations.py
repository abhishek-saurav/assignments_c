import datetime
import calendar

city = input("Enter your city name: ")
now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)
print(calendar.calendar(now.year))
