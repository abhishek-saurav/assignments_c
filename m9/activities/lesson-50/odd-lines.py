file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

out = open("odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saved to odd-lines.txt")
