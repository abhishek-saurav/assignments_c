name = "Sam"
hobbies = ["chess", "photography", "guitar", "coding"]

print(name + "'s hobbies:")
for hobby in hobbies:
    print("-", hobby)

target = "guitar"
found = False
for hobby in hobbies:
    if hobby == target:
        found = True
if found:
    print(target, "is one of", name + "'s hobbies")
else:
    print(target, "is not in the list")
