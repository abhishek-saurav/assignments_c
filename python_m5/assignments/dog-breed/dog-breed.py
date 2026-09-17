class Dog:
    animal_type = "Canine"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

dog1 = Dog("Rocky", "Labrador", 3)
dog2 = Dog("Bruno", "German Shepherd", 5)

print("Owner: Abhishek")
print(f"{dog1.name} is a {dog1.breed} and is a {dog1.animal_type}")
print(f"{dog2.name} is a {dog2.breed} and is a {dog2.animal_type}")
print(f"{dog1.name} is {dog1.age} years old")
print(f"{dog2.name} is {dog2.age} years old")
