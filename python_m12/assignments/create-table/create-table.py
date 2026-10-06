import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    department TEXT NOT NULL,
    city TEXT NOT NULL,
    salary INTEGER NOT NULL
)""")
cur.execute("""INSERT INTO employee (emp_id, emp_name, department, city, salary) VALUES
(1, 'Rohan Mehta', 'Accounts', 'Delhi', 52000),
(2, 'Priya Nair', 'Accounts', 'Mumbai', 61000),
(3, 'Karan Singh', 'Audit', 'Delhi', 48000),
(4, 'Sneha Rao', 'Audit', 'Bangalore', 55000),
(5, 'Vikram Das', 'Procurement', 'Delhi', 70000),
(6, 'Anita Joshi', 'Procurement', 'Mumbai', 45000)""")

print("All employees:")
cur.execute("""SELECT * FROM employee""")
for row in cur.fetchall():
    print(row)
print()

print("Names and cities:")
cur.execute("""SELECT emp_name, city FROM employee""")
for row in cur.fetchall():
    print(row)
print()

print("Employees in Delhi:")
cur.execute("""SELECT * FROM employee WHERE city = 'Delhi'""")
for row in cur.fetchall():
    print(row)
print()

print("Employees earning more than 50000:")
cur.execute("""SELECT emp_name, department, salary FROM employee WHERE salary > 50000""")
for row in cur.fetchall():
    print(row)
print()

print("Audit department:")
cur.execute("""SELECT * FROM employee WHERE department = 'Audit'""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
