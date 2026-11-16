import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

conn.execute("""CREATE TABLE teacher (
    teacher_id INTEGER PRIMARY KEY,
    teacher_name TEXT NOT NULL UNIQUE
)""")
conn.execute("""CREATE TABLE subject (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL,
    teacher_id INTEGER
)""")
conn.executemany("INSERT INTO teacher VALUES (?, ?)", [
    (1, 'Abhishek'),
    (2, 'Mrs. Rao'),
    (3, 'Mr. Dsouza'),
    (4, 'Ms. Fernandes'),
])
conn.executemany("INSERT INTO subject VALUES (?, ?, ?)", [
    (1, 'Python', 1),
    (2, 'SQL', 1),
    (3, 'Maths', 2),
    (4, 'Science', 3),
    (5, 'English', 3),
])
conn.commit()

inner = pd.read_sql("SELECT teacher.teacher_name, subject.subject_name "
                    "FROM teacher INNER JOIN subject ON teacher.teacher_id = subject.teacher_id", conn)
print("INNER JOIN - teachers matched with their subjects:")
print(inner)
print()

left = pd.read_sql("SELECT teacher.teacher_name, subject.subject_name "
                   "FROM teacher LEFT JOIN subject ON teacher.teacher_id = subject.teacher_id", conn)
print("LEFT JOIN - all teachers, NULL where no subject found:")
print(left)
print()

cross = pd.read_sql("SELECT teacher.teacher_name, subject.subject_name "
                    "FROM teacher CROSS JOIN subject WHERE teacher.teacher_id <= 2", conn)
print("CROSS JOIN - first 2 teachers paired with every subject:")
print(cross)
print()

union = pd.read_sql("SELECT teacher_name AS name, 'Teacher' AS type FROM teacher "
                    "UNION "
                    "SELECT subject_name AS name, 'Subject' AS type FROM subject", conn)
print("UNION - all teacher names and subject names combined:")
print(union)

conn.close()
