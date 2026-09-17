class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print(f"blu is a {blu.species}")
print(f"woo is a {woo.species}")
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")
