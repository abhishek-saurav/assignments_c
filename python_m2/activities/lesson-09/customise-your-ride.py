print("=== Welcome to Ride Builder! ===")

print("1 - Bike")
print("2 - Car")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("1 - Scooty")
    print("2 - Mountain Bike")
    bike_type = int(input("Enter your choice: "))
    if bike_type == 1:
        print("Scooty — Top speed: 80 km/h — Best for: City roads")
    else:
        print("Mountain Bike — Top speed: 40 km/h — Best for: Off-road trails")
elif choice == 2:
    print("1 - Sedan")
    print("2 - SUV")
    car_type = int(input("Enter your choice: "))
    if car_type == 1:
        print("Sedan — Seats: 5 — Best for: Family trips")
    else:
        print("SUV — Seats: 7 — Best for: Off-road adventures")
else:
    print("That was not a valid choice.")

print("=== Your custom ride is ready! ===")
