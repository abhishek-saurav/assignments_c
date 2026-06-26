file = open("notes.txt", "w")
file.write("Python is fun\n")
file.write("File handling is useful\n")
file.close()
print("Write mode: File created and written.")

file = open("notes.txt", "r")
content = file.read()
print("\nRead mode:")
print(content)
file.close()

file = open("notes.txt", "a")
file.write("Append mode adds new content\n")
file.close()
print("Append mode: New line added.")

file = open("notes.txt", "r")
lines = file.readlines()
file.close()
print("\nFinal file content:")
for i in range(len(lines)):
    print(f"Line {i + 1}: {lines[i].strip()}")
