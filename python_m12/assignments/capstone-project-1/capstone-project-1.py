import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    department TEXT NOT NULL,
    job TEXT NOT NULL,
    salary INTEGER NOT NULL,
    bonus INTEGER,
    hire_year INTEGER NOT NULL
)""")
cur.execute("""INSERT INTO employee (emp_id, emp_name, department, job, salary, bonus, hire_year) VALUES
(1, 'Harsh Verma', 'Sales', 'Manager', 90000, 10000, 2015),
(2, 'Asha Patel', 'Sales', 'Executive', 45000, NULL, 2019),
(3, 'Ravi Kumar', 'Sales', 'Executive', 47000, 2000, 2018),
(4, 'Neha Sharma', 'IT', 'Developer', 80000, 5000, 2017),
(5, 'Imran Khan', 'IT', 'Developer', 72000, NULL, 2020),
(6, 'Divya Iyer', 'IT', 'Manager', 110000, 15000, 2014),
(7, 'Sameer Joshi', 'HR', 'Executive', 40000, NULL, 2021),
(8, 'Meera Das', 'HR', 'Manager', 85000, 7000, 2016)""")

print("All employees:")
cur.execute("""SELECT * FROM employee""")
for row in cur.fetchall():
    print(row)
print()

print("Highest salary first:")
cur.execute("""SELECT emp_name, department, salary FROM employee ORDER BY salary DESC""")
for row in cur.fetchall():
    print(row)
print()

print("Salary between 45000 and 85000:")
cur.execute("""SELECT emp_name, salary FROM employee WHERE salary BETWEEN 45000 AND 85000""")
for row in cur.fetchall():
    print(row)
print()

print("Employees without a bonus:")
cur.execute("""SELECT emp_name, department FROM employee WHERE bonus IS NULL""")
for row in cur.fetchall():
    print(row)
print()

print("Employees with a bonus:")
cur.execute("""SELECT emp_name, bonus FROM employee WHERE bonus IS NOT NULL""")
for row in cur.fetchall():
    print(row)
print()

print("Managers in Sales or IT:")
cur.execute("""SELECT emp_name, department, job FROM employee WHERE job = 'Manager' AND (department = 'Sales' OR department = 'IT')""")
for row in cur.fetchall():
    print(row)
print()

print("Distinct departments:")
cur.execute("""SELECT DISTINCT department FROM employee""")
for row in cur.fetchall():
    print(row)
print()

print("Employees and average salary per department:")
cur.execute("""SELECT department, COUNT(*) AS total_employees, AVG(salary) AS average_salary FROM employee GROUP BY department""")
for row in cur.fetchall():
    print(row)
print()

print("Departments with an average salary above 65000:")
cur.execute("""SELECT department, AVG(salary) AS average_salary FROM employee GROUP BY department HAVING AVG(salary) > 65000""")
for row in cur.fetchall():
    print(row)
print()

print("Top 3 earners:")
cur.execute("""SELECT emp_name, salary FROM employee ORDER BY salary DESC LIMIT 3""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
