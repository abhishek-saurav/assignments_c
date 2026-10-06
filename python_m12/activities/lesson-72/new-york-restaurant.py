import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Restaurant (
    name TEXT,
    neighborhood TEXT,
    cuisine TEXT,
    review REAL,
    price TEXT,
    health TEXT
)""")
cur.execute("""INSERT INTO Restaurant (name, neighborhood, cuisine, review, price, health) VALUES
('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
('Pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),
('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$', 'A'),
('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A')""")

print("1) Distinct neighborhoods:")
cur.execute("""SELECT DISTINCT neighborhood FROM Restaurant""")
for row in cur.fetchall():
    print(row)
print()

print("2) Distinct cuisine types:")
cur.execute("""SELECT DISTINCT cuisine FROM Restaurant""")
for row in cur.fetchall():
    print(row)
print()

print("3) Chinese takeout options:")
cur.execute("""SELECT * FROM Restaurant WHERE cuisine = 'Chinese'""")
for row in cur.fetchall():
    print(row)
print()

print("4) Reviews of 4 and above:")
cur.execute("""SELECT * FROM Restaurant WHERE review >= 4.0""")
for row in cur.fetchall():
    print(row)
print()

print("5) Italian restaurants priced $$ or $$$:")
cur.execute("""SELECT * FROM Restaurant WHERE cuisine = 'Italian' AND price IN ('$$', '$$$')""")
for row in cur.fetchall():
    print(row)
print()

print("6) Restaurants with exactly $$$:")
cur.execute("""SELECT * FROM Restaurant WHERE price = '$$$'""")
for row in cur.fetchall():
    print(row)
print()

print("7) Names containing Candy:")
cur.execute("""SELECT * FROM Restaurant WHERE name LIKE '%Candy%'""")
for row in cur.fetchall():
    print(row)
print()

print("8) Midtown, Downtown or Chinatown:")
cur.execute("""SELECT * FROM Restaurant WHERE neighborhood IN ('Midtown', 'Downtown', 'Chinatown')""")
for row in cur.fetchall():
    print(row)
print()

print("9) Health grade pending:")
cur.execute("""SELECT * FROM Restaurant WHERE health = '' OR health IS NULL""")
for row in cur.fetchall():
    print(row)
print()

print("10) Top 4 restaurants by review:")
cur.execute("""SELECT * FROM Restaurant ORDER BY review DESC LIMIT 4""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
