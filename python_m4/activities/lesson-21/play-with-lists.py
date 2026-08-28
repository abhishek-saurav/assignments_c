L = [12, 45, 7, 23, 56, 89, 34]
print("Original list:", L)

count = 0
for i in range(len(L)):
    count = count + L[i]

avg = count / len(L)
print("Sum:", count)
print("Average:", avg)

L.sort()
print("Smallest:", L[0])
print("Largest:", L[-1])
