file = open("class-notes.txt", "w")
file.write("Maths: Learn equations today\n")
file.write("Coding: Variables and loops\n")
file.write("Science: Photosynthesis\n")
file.write("Coding: If statements\n")
file.write("English: Essay writing\n")
file.write("Coding: Functions and recursion\n")
file.write("History: World War II\n")
file.close()

n = int(input("How many characters to preview? "))
file = open("class-notes.txt", "r")
print(file.read(n))
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

word = input("Skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saved to odd-lines.txt")
