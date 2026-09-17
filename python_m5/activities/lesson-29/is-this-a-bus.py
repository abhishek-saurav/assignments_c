class Vehicle:
    def __init__(self, name):
        self.name = name

class Bus(Vehicle):
    def __init__(self, name, seats):
        super().__init__(name)
        self.seats = seats

bus1 = Bus("School Bus", 40)
car1 = Vehicle("Sedan")

print("Is bus1 a Bus?", isinstance(bus1, Bus))
print("Is car1 a Bus?", isinstance(car1, Bus))
print("Is Bus a subclass of Vehicle?", issubclass(Bus, Vehicle))
