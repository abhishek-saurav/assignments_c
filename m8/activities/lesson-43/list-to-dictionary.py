# Two related lists
roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]

# Convert to a dictionary using zip()
students = dict(zip(roll_numbers, names))
print(students)
# {1: 'Aarav', 2: 'Priya', 3: 'Rahul', 4: 'Sneha', 5: 'Dev'}

# Look up a student by roll number
print(students[3])   # Rahul
