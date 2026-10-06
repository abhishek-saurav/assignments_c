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
cur.execute("""CREATE TABLE customer (
    customer_id TEXT PRIMARY KEY,
    cust_name TEXT,
    city TEXT,
    grade INTEGER,
    salesman_id TEXT
)""")
cur.execute("""INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES
('3002', 'nick rimando', 'New York', 100, '5001'),
('3007', 'brad davis', 'New York', 200, '5001'),
('3005', 'graham zusi', 'California', 200, '5002'),
('3008', 'julian green', 'London', 300, '5002'),
('3004', 'fabian johnson', 'Paris', 300, '5006'),
('3009', 'geoff cameron', 'Berlin', 100, '5003'),
('3003', 'jozy altidor', 'Moscow', 200, '5007'),
('3001', 'brad guzan', 'London', NULL, '5005')""")
cur.execute("""CREATE TABLE orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT
)""")
cur.execute("""INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
('70001', 150.5, '2012-10-05', '3005', '5002'),
('70009', 270.65, '2012-09-10', '3001', '5001'),
('70002', 65.26, '2012-10-05', '3002', '5003'),
('70004', 110.5, '2012-08-17', '3009', '5007'),
('70007', 948.5, '2012-09-10', '3005', '5005'),
('70005', 2400.6, '2012-07-27', '3007', '5006')""")

print("Customers and salesmen from the same city:")
cur.execute("""SELECT customer.cust_name, salesman.name, salesman.city FROM customer JOIN salesman ON customer.city = salesman.city""")
for row in cur.fetchall():
    print(row)
print()

print("Customers and their salesmen:")
cur.execute("""SELECT customer.cust_name, salesman.name FROM customer JOIN salesman ON customer.salesman_id = salesman.salesman_id""")
for row in cur.fetchall():
    print(row)
print()

print("Orders where the customer city and salesman city differ:")
cur.execute("""SELECT orders.ord_no, customer.cust_name, orders.customer_id, orders.salesman_id FROM orders JOIN customer ON orders.customer_id = customer.customer_id JOIN salesman ON orders.salesman_id = salesman.salesman_id WHERE customer.city <> salesman.city""")
for row in cur.fetchall():
    print(row)
print()

print("All orders with customer names:")
cur.execute("""SELECT orders.ord_no, customer.cust_name FROM orders JOIN customer ON orders.customer_id = customer.customer_id""")
for row in cur.fetchall():
    print(row)
print()

print("Customers that have a grade:")
cur.execute("""SELECT cust_name, grade FROM customer WHERE grade IS NOT NULL""")
for row in cur.fetchall():
    print(row)
print()

print("Customers and salesmen with commission between 0.12 and 0.14:")
cur.execute("""SELECT customer.cust_name, customer.city, salesman.name, salesman.commission FROM customer JOIN salesman ON customer.salesman_id = salesman.salesman_id WHERE salesman.commission BETWEEN 0.12 AND 0.14""")
for row in cur.fetchall():
    print(row)
print()

print("Commission on orders of customers with grade 200 or more:")
cur.execute("""SELECT orders.ord_no, customer.cust_name, salesman.commission, orders.purch_amt * salesman.commission AS commission_amount FROM orders JOIN salesman ON orders.salesman_id = salesman.salesman_id JOIN customer ON orders.customer_id = customer.customer_id WHERE customer.grade >= 200""")
for row in cur.fetchall():
    print(row)
print()

print("Orders placed on 2012-10-05:")
cur.execute("""SELECT * FROM customer JOIN orders ON customer.customer_id = orders.customer_id WHERE orders.ord_date = '2012-10-05'""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
