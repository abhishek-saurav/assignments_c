monday = {"math", "science", "english", "art", "music"}
tuesday = {"math", "history", "english", "sports", "computer"}

print("Monday:", monday)
print("Tuesday:", tuesday)

result = monday.symmetric_difference(tuesday)
print("Subjects on only one day:", result)
