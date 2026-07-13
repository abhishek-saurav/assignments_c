text = input("Enter a string: ")

substrings = []
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        substrings.append(text[i:j])

print("All substrings of", text + ":")
for s in substrings:
    print(s)
print("Total substrings:", len(substrings))
