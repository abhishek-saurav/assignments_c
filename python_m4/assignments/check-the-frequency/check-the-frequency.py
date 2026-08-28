marks = {"math": 85, "science": 90, "english": 85, "history": 78, "art": 85}
print("Marks:", marks)

target = 85
count = 0
for subject in marks:
    if marks[subject] == target:
        count = count + 1

print("Number of subjects scoring", target, "is", count)
