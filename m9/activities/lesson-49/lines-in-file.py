file = open("bucket-list.txt", "r")
lines = file.readlines()
file.close()

print("=== Lines in File ===")
for i in range(len(lines)):
    print(f"Line {i + 1}: {lines[i].strip()}")

print(f"\nTotal lines: {len(lines)}")
