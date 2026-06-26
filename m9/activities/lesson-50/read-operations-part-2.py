file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
