import os

science_notes = [
    "Plants need sunlight and water\n",
    "The Earth moves around the Sun\n",
    "Water can change into ice and steam\n"
]

maths_notes = [
    "Addition means finding the total\n",
    "Subtraction means taking away\n",
    "Multiplication is repeated addition\n"
]

with open("science-notes.txt", "w") as f:
    f.writelines(science_notes)

with open("maths-notes.txt", "w") as f:
    f.writelines(maths_notes)

print("=== Science Notes ===")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())

print("\n=== Word Count (Maths Notes) ===")
with open("maths-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())

print("\n=== Merging Notes ===")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists - overwriting")
else:
    print("all-notes.txt not found - creating now")

content = ""
with open("science-notes.txt", "r") as f:
    content += "--- science-notes.txt ---\n"
    content += f.read() + "\n"
with open("maths-notes.txt", "r") as f:
    content += "--- maths-notes.txt ---\n"
    content += f.read() + "\n"

with open("all-notes.txt", "w") as out:
    out.write(content)
print("Saved to all-notes.txt")

if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("all-notes.txt deleted.")
