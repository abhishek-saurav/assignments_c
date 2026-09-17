class Vehicle:
    def __init__(self, distance):
        self.distance = distance

class Bus(Vehicle):
    def __init__(self, distance, fare_per_km):
        super().__init__(distance)
        self.fare_per_km = fare_per_km

    def calculate_fare(self):
        return self.distance * self.fare_per_km

bus1 = Bus(25, 3)
print("Passenger: Abhishek")
print("Distance:", bus1.distance, "km")
print("Fare per km:", bus1.fare_per_km)
print("Total fare:", bus1.calculate_fare())
