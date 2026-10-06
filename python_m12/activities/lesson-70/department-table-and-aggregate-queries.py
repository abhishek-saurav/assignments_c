import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE department (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL,
    location TEXT NOT NULL,
    employees INTEGER NOT NULL,
    budget INTEGER NOT NULL
)""")
cur.execute("""INSERT INTO department VALUES
(1, 'Sales', 'Mumbai', 25, 500000),
(2, 'Marketing', 'Mumbai', 15, 350000),
(3, 'Engineering', 'Bangalore', 60, 1500000),
(4, 'Support', 'Bangalore', 30, 400000),
(5, 'Finance', 'Delhi', 12, 450000),
(6, 'HR', 'Delhi', 8, 200000),
(7, 'Research', 'Bangalore', 20, 900000)""")

print("All departments:")
cur.execute("""SELECT * FROM department""")
for row in cur.fetchall():
    print(row)
print()

print("Number of departments:")
cur.execute("""SELECT COUNT(dept_id) AS total_departments FROM department""")
for row in cur.fetchall():
    print(row)
print()

print("Total employees and total budget:")
cur.execute("""SELECT SUM(employees) AS total_employees, SUM(budget) AS total_budget FROM department""")
for row in cur.fetchall():
    print(row)
print()

print("Average budget:")
cur.execute("""SELECT AVG(budget) AS average_budget FROM department""")
for row in cur.fetchall():
    print(row)
print()

print("Lowest and highest budget:")
cur.execute("""SELECT MIN(budget) AS lowest_budget, MAX(budget) AS highest_budget FROM department""")
for row in cur.fetchall():
    print(row)
print()

print("Departments and employees per location:")
cur.execute("""SELECT location, COUNT(*) AS departments, SUM(employees) AS total_employees FROM department GROUP BY location""")
for row in cur.fetchall():
    print(row)
print()

print("Locations with an average budget of at least 500000:")
cur.execute("""SELECT location, AVG(budget) AS average_budget FROM department GROUP BY location HAVING AVG(budget) >= 500000 ORDER BY average_budget DESC""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
