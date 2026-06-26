file = open("bucket-list.txt", "r")
lines = file.readlines()
file.close()

print(f"You have {len(lines)} items on your bucket list.")
print(lines)
print("First item:", lines[0].strip())
print("Last item:", lines[-1].strip())
