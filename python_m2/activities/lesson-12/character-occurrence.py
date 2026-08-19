text = input("Enter a word: ")

n = len(text)
for i in range(n):
    count = 0
    for j in range(n):
        if text[j] == text[i]:
            count += 1
    print(text[i], "appears", count, "times")
