locker_code = 12
backup_code = 12

print("Is the code an int?", type(locker_code) is int)
print("Is the code not a float?", type(locker_code) is not float)
print("Do both codes share one identity?", locker_code is backup_code)

backup_code = 30
print("Do they have different identity now?", locker_code is not backup_code)

allowed_items = ["camera", "guitar", "chess board", "laptop"]
blocked_items = ["scissors", "matchbox"]

print("Allowed items:", allowed_items)
item = input("Which item are you storing? ")

if item in allowed_items:
    print(item, "is allowed in the locker")
elif item in blocked_items:
    print(item, "is blocked at St. Alberts")
else:
    print(item, "is not on any list. Ask the class teacher.")

owner = "Abhishek"
print("Is 'bhi' inside the owner name?", "bhi" in owner)
print("Is 'xyz' missing from the owner name?", "xyz" not in owner)

a = 12
b = 10

print("a & b  =", a & b)
print("a | b  =", a | b)
print("a ^ b  =", a ^ b)
print("~b     =", ~b)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
