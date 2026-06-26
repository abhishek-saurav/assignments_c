student = {"name": "Aarav", "age": 13, "grade": 7}

# Safe access using .get()  -  no error if key is missing
print(student.get("age"))               # 13
print(student.get("school", "N/A"))     # N/A

# Update an existing value
student["age"] = 14

# Add a new key-value pair
student["school"] = "Sunrise Academy"
print(student)
# {'name': 'Aarav', 'age': 14, 'grade': 7, 'school': 'Sunrise Academy'}

# Remove a specific key
student.pop("grade")
print(student)
# {'name': 'Aarav', 'age': 14, 'school': 'Sunrise Academy'}

# Clear the entire dictionary
student.clear()
print(student)   # {}
