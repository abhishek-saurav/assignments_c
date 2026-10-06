import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE customer_export (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    product TEXT NOT NULL,
    country TEXT NOT NULL,
    quantity INTEGER NOT NULL
)""")
cur.execute("""INSERT INTO customer_export (customer_id, customer_name, product, country, quantity) VALUES
(1, 'Alfred Traders', 'Tea', 'Germany', 120),
(2, 'Amora Foods', 'Spices', 'France', 80),
(3, 'Anton Stores', 'Rice', 'Mexico', 200),
(4, 'Berglund Corp', 'Tea', 'Sweden', 60),
(5, 'Ana Trading', 'Coffee', 'Spain', 90),
(6, 'Victoria Exports', 'Spices', 'Germany', 150),
(7, 'Around Horn', 'Rice', 'UK', 110),
(8, 'Worldwide Imports', 'Coffee', 'France', 70),
(9, 'Aurora Mart', 'Tea', 'Canada', 130)""")

print("All customers:")
cur.execute("""SELECT * FROM customer_export""")
for row in cur.fetchall():
    print(row)
print()

print("Customers whose name starts with a:")
cur.execute("""SELECT * FROM customer_export WHERE customer_name LIKE 'a%'""")
for row in cur.fetchall():
    print(row)
print()

print("Customers whose name contains or:")
cur.execute("""SELECT * FROM customer_export WHERE customer_name LIKE '%or%'""")
for row in cur.fetchall():
    print(row)
print()

print("Customers starting with a and containing or:")
cur.execute("""SELECT * FROM customer_export WHERE customer_name LIKE 'a%' AND customer_name LIKE '%or%'""")
for row in cur.fetchall():
    print(row)
print()

print("Distinct products:")
cur.execute("""SELECT DISTINCT product FROM customer_export""")
for row in cur.fetchall():
    print(row)
print()

print("Distinct countries exported to:")
cur.execute("""SELECT DISTINCT country FROM customer_export""")
for row in cur.fetchall():
    print(row)
print()

print("Products and countries for each customer, largest quantity first:")
cur.execute("""SELECT customer_name, product, country, quantity FROM customer_export ORDER BY quantity DESC""")
for row in cur.fetchall():
    print(row)
print()

print("Top 3 customers by quantity:")
cur.execute("""SELECT customer_name, quantity FROM customer_export ORDER BY quantity DESC LIMIT 3""")
for row in cur.fetchall():
    print(row)
print()

print("Customers per country:")
cur.execute("""SELECT country, COUNT(*) AS customers FROM customer_export GROUP BY country HAVING COUNT(*) > 1""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
