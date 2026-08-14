name = "Abhishek"
school = "St. Alberts"

print("Full name:", name)
print("First letter:", name[0])
print("Letter at position 3:", name[3])
print("Last letter:", name[-1])

print("First four letters:", name[0:4])
print("From position 4 onwards:", name[4:])
print("Reversed name:", name[::-1])

joined = name + " of " + school
print("Joined together:", joined)
print("In capitals:", joined.upper())
