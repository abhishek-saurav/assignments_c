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
conn.execute("INSERT INTO Student VALUES (1, 'Abhishek', 'St. Alberts', 31, 'Photography');")
conn.execute("INSERT INTO Student VALUES (2, 'Rohan', 'St. Alberts', 30, 'Guitar');")
conn.execute("INSERT INTO Student (Student_Id, Student_Name, School) VALUES (3, 'Kabir', 'St. Marys');")
conn.commit()

print("\n--- Testing PRIMARY KEY ---")
try:
    conn.execute("INSERT INTO Student VALUES (1, 'Meera', 'St. Marys', 29, 'Coding');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Student_Id 1 already belongs to Abhishek — PRIMARY KEY must be unique.")

print("\n--- Testing NOT NULL ---")
try:
    conn.execute("INSERT INTO Student VALUES (4, 'Meera', NULL, 29, 'Coding');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("School is NOT NULL — every row must provide a school value.")

print("\n--- Testing UNIQUE ---")
try:
    conn.execute("INSERT INTO Student VALUES (5, 'Abhishek', 'St. Johns', 25, 'Chess');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Student_Name is UNIQUE — 'Abhishek' is already in the table.")

print("\n--- DEFAULT value check for Kabir ---")
kabir = pd.read_sql("""SELECT Student_Name, School, Hobby
    FROM Student
    WHERE Student_Name == 'Kabir';""", conn)
print(kabir)
print("Hobby was not given — DEFAULT 'Chess' was used automatically.")

conn.close()
