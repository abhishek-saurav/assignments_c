from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("I move on roads with four wheels")

class Bike(Vehicle):
    def move(self):
        print("I move on roads with two wheels")

class Boat(Vehicle):
    def move(self):
        print("I move on water")

vehicles = [Car(), Bike(), Boat()]

for vehicle in vehicles:
    vehicle.move()
