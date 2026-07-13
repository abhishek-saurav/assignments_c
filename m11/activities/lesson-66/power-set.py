n = int(input("How many elements in the set? "))
elements = []
for i in range(n):
    elem = input("Enter element " + str(i + 1) + ": ")
    elements.append(elem)

total = 1 << n
print("Power set of", elements, ":")
for i in range(total):
    subset = []
    for j in range(n):
        if i & (1 << j) != 0:
            subset.append(elements[j])
    print(subset)

print("Total subsets:", total)
