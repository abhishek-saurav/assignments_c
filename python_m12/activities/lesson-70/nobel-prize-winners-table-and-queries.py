import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE nobel_winners (
    year INTEGER NOT NULL,
    subject TEXT NOT NULL,
    winner TEXT NOT NULL,
    country TEXT NOT NULL
)""")
cur.execute("""INSERT INTO nobel_winners VALUES
(1970, 'Physics', 'Hannes Alfven', 'Sweden'),
(1970, 'Physics', 'Louis Neel', 'France'),
(1970, 'Chemistry', 'Luis Federico Leloir', 'Argentina'),
(1970, 'Medicine', 'Julius Axelrod', 'USA'),
(1971, 'Physics', 'Dennis Gabor', 'UK'),
(1971, 'Chemistry', 'Gerhard Herzberg', 'Canada'),
(1971, 'Literature', 'Pablo Neruda', 'Chile'),
(1971, 'Medicine', 'Earl Sutherland', 'USA'),
(1972, 'Physics', 'John Bardeen', 'USA'),
(1972, 'Chemistry', 'Christian Anfinsen', 'USA'),
(1972, 'Medicine', 'Gerald Edelman', 'USA'),
(1972, 'Literature', 'Heinrich Boll', 'Germany')""")

print("All winners, newest year first:")
cur.execute("""SELECT * FROM nobel_winners ORDER BY year DESC""")
for row in cur.fetchall():
    print(row)
print()

print("Sorted by subject, then year:")
cur.execute("""SELECT subject, year, winner FROM nobel_winners ORDER BY subject ASC, year DESC""")
for row in cur.fetchall():
    print(row)
print()

print("First 3 winners from 1970:")
cur.execute("""SELECT year, subject, winner FROM nobel_winners WHERE year = 1970 ORDER BY winner ASC LIMIT 3""")
for row in cur.fetchall():
    print(row)
print()

print("Winners per subject:")
cur.execute("""SELECT subject, COUNT(*) AS total_winners FROM nobel_winners GROUP BY subject""")
for row in cur.fetchall():
    print(row)
print()

print("Winners per country:")
cur.execute("""SELECT country, COUNT(*) AS total_winners FROM nobel_winners GROUP BY country ORDER BY total_winners DESC""")
for row in cur.fetchall():
    print(row)
print()

print("Subjects with more than 2 winners:")
cur.execute("""SELECT subject, COUNT(*) AS total_winners FROM nobel_winners GROUP BY subject HAVING COUNT(*) > 2""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
