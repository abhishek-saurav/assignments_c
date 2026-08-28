test_dict = {"gfg": 1, "is": 2, "best": 3, "for": 2, "geeks": 2}
print("Original dictionary:", test_dict)

K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of", K, "is", res)
