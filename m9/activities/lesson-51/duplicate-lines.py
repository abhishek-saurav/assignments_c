import os

with open("notes.txt", "w") as f:
    f.write("Python is fun\n")
    f.write("File handling is useful\n")
    f.write("Python is fun\n")
    f.write("Loops help repeat tasks\n")
    f.write("File handling is useful\n")

with open("notes.txt", "r") as f:
    lines = f.readlines()

seen = []
unique_lines = []
for line in lines:
    if line not in seen:
        seen.append(line)
        unique_lines.append(line)

with open("notes-clean.txt", "w") as f:
    f.writelines(unique_lines)

print("Duplicate lines removed.")
print("Unique lines:")
for line in unique_lines:
    print(line.strip())
