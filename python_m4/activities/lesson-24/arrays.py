import array as arr

scores = arr.array('i', [10, 20, 30, 20, 40])
print("Scores:", scores)

scores.insert(0, 5)
print("After insert:", scores)

scores.append(50)
print("After append:", scores)

print("Times 20 appears:", scores.count(20))

scores.reverse()
print("Reversed:", scores)
