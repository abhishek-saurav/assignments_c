import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS zoo_animal (
    animal_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age_years INTEGER NOT NULL,
    weight_kg REAL NOT NULL
)""")
cur.execute("""INSERT INTO zoo_animal VALUES
(1, 'Lion', 'Big Cat', 5, 190.0),
(2, 'Tiger', 'Big Cat', 3, 220.0),
(3, 'Elephant', 'Pachyderm', 12, 4500.0),
(4, 'Giraffe', 'Ungulate', 7, 800.0),
(5, 'Penguin', 'Bird', 2, 5.0),
(6, 'Panda', 'Bear', 6, 95.0),
(7, 'Cheetah', 'Big Cat', 4, 55.0),
(8, 'Rhino', 'Pachyderm', 9, 2300.0)""")

print("All animals:")
cur.execute("""SELECT * FROM zoo_animal""")
for row in cur.fetchall():
    print(row)
print()

print("All species:")
cur.execute("""SELECT species FROM zoo_animal""")
for row in cur.fetchall():
    print(row)
print()

print("Unique species:")
cur.execute("""SELECT DISTINCT species FROM zoo_animal""")
for row in cur.fetchall():
    print(row)
print()

print("Number of unique species:")
cur.execute("""SELECT COUNT(DISTINCT species) AS unique_species FROM zoo_animal""")
for row in cur.fetchall():
    print(row)
print()

print("Total animals:")
cur.execute("""SELECT COUNT(animal_id) AS total_animals FROM zoo_animal""")
for row in cur.fetchall():
    print(row)
print()

print("Animals older than 5 years:")
cur.execute("""SELECT COUNT(animal_id) AS older_than_5 FROM zoo_animal WHERE age_years > 5""")
for row in cur.fetchall():
    print(row)
print()

print("Total weight:")
cur.execute("""SELECT SUM(weight_kg) AS total_weight_kg FROM zoo_animal""")
for row in cur.fetchall():
    print(row)
print()

print("Average age:")
cur.execute("""SELECT AVG(age_years) AS avg_age_years FROM zoo_animal""")
for row in cur.fetchall():
    print(row)
print()

print("Zoo summary:")
cur.execute("""SELECT COUNT(animal_id) AS total_animals, COUNT(DISTINCT species) AS unique_species, SUM(weight_kg) AS total_weight_kg, AVG(age_years) AS avg_age_years FROM zoo_animal""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
