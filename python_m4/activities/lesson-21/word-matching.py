def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr = ctr + 1
            lst.append(word)
    print(lst)
    return ctr


words = ["aba", "xyz", "1231", "level", "cat", "gig"]
count = match_words(words)
print("Matching words:", count)
