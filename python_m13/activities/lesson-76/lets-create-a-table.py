import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

conn.execute("""
CREATE TABLE Student (
    Student_Id INTEGER PRIMARY KEY,
    Student_Name TEXT NOT NULL UNIQUE,
    School TEXT NOT NULL,
    Age INTEGER,
    Hobby TEXT DEFAULT 'Chess'
);
""")
conn.commit()
print("Table created successfully!")

conn.execute("INSERT INTO Student VALUES (1, 'Abhishek', 'St. Alberts', 31, 'Photography');")
conn.execute("INSERT INTO Student VALUES (2, 'Rohan', 'St. Alberts', 30, 'Guitar');")
conn.execute("INSERT INTO Student VALUES (3, 'Meera', 'St. Marys', 29, 'Coding');")
conn.execute("INSERT INTO Student (Student_Id, Student_Name, School) VALUES (4, 'Kabir', 'St. Marys');")
conn.commit()
print("Rows inserted successfully!")

students = pd.read_sql("SELECT * FROM Student;", conn)
print(students)

conn.close()
