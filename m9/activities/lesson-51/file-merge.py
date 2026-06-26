import os

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
