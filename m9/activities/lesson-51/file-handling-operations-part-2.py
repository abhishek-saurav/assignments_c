with open("maths-notes.txt", "w") as f:
    f.write("Triangles have three sides\n")
    f.write("Pi is 3.14\n")
    f.write("Area equals length times width\n")
    f.write("Prime numbers divide only by one\n")

print("=== Word Count ===")
with open("maths-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
