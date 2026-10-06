import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE salesman (
    salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commission REAL
)""")
cur.execute("""INSERT INTO salesman (salesman_id, name, city, commission) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002', 'Nail Knite', 'Paris', 0.13),
('5003', 'Lauson Hen', 'San Jose', 0.12),
('5005', 'Pit Alex', 'London', 0.11),
('5006', 'Mc Lyon', 'Paris', 0.14),
('5007', 'Paul Adam', 'Rome', 0.13)""")
cur.execute("""CREATE TABLE orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT
)""")
cur.execute("""INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
('70001', 150.5, '2012-10-05', '3005', '5002'),
('70002', 65.26, '2012-10-05', '3002', '5003'),
('70004', 110.5, '2012-08-17', '3009', '5007'),
('70005', 2400.6, '2012-07-27', '3007', '5006'),
('70007', 948.5, '2012-09-10', '3005', '5005'),
('70009', 270.65, '2012-09-10', '3001', '5001'),
('70011', 75.29, '2012-08-17', '3003', '5005')""")

print("Salesmen:")
cur.execute("""SELECT * FROM salesman""")
for row in cur.fetchall():
    print(row)
print()

print("Orders:")
cur.execute("""SELECT * FROM orders""")
for row in cur.fetchall():
    print(row)
print()

cur.execute("""SELECT salesman_id FROM salesman WHERE city = 'London'""")
london_id = cur.fetchone()[0]

print("Orders of the London salesman:")
cur.execute("SELECT * FROM orders WHERE salesman_id = '" + london_id + "'")
for row in cur.fetchall():
    print(row)
print()

conn.close()
