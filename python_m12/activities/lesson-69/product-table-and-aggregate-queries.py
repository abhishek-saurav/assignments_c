import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price INTEGER NOT NULL,
    quantity INTEGER NOT NULL
)""")
cur.execute("""INSERT INTO product VALUES
(1, 'Acoustic Guitar', 'String', 8500, 4),
(2, 'Electric Guitar', 'String', 22000, 2),
(3, 'Ukulele', 'String', 3200, 6),
(4, 'Keyboard', 'Keys', 15000, 3),
(5, 'Drum Pad', 'Percussion', 6500, 5),
(6, 'Bongo', 'Percussion', 2800, 7),
(7, 'Flute', 'Wind', 1200, 10),
(8, 'Harmonica', 'Wind', 600, 12)""")

print("All products:")
cur.execute("""SELECT * FROM product""")
for row in cur.fetchall():
    print(row)
print()

print("Distinct categories:")
cur.execute("""SELECT DISTINCT category FROM product""")
for row in cur.fetchall():
    print(row)
print()

print("Number of products:")
cur.execute("""SELECT COUNT(product_id) AS total_products FROM product""")
for row in cur.fetchall():
    print(row)
print()

print("Products costing more than 5000:")
cur.execute("""SELECT COUNT(product_id) AS above_5000 FROM product WHERE price > 5000""")
for row in cur.fetchall():
    print(row)
print()

print("Total stock:")
cur.execute("""SELECT SUM(quantity) AS total_stock FROM product""")
for row in cur.fetchall():
    print(row)
print()

print("Average price:")
cur.execute("""SELECT AVG(price) AS average_price FROM product""")
for row in cur.fetchall():
    print(row)
print()

print("Lowest and highest price:")
cur.execute("""SELECT MIN(price) AS lowest_price, MAX(price) AS highest_price FROM product""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
