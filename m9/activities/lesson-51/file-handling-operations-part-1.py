with open("science-notes.txt", "w") as f:
    f.write("Planets orbit the Sun\n")
    f.write("The Moon causes tides\n")
    f.write("Light is faster than sound\n")
    f.write("Plants convert sunlight to food\n")

print("=== Science Notes ===")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
