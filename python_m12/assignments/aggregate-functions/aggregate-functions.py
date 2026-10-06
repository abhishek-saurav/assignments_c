import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS marine_observation (
    observation_id INTEGER PRIMARY KEY,
    animal_name TEXT NOT NULL,
    animal_group TEXT NOT NULL,
    habitat TEXT NOT NULL,
    depth_m INTEGER NOT NULL,
    estimated_weight_kg REAL NOT NULL
)""")
cur.execute("""INSERT INTO marine_observation VALUES
(1, 'Blue Whale', 'Mammal', 'Open Ocean', 30, 120000.0),
(2, 'Bottlenose Dolphin', 'Mammal', 'Open Ocean', 15, 250.0),
(3, 'Green Sea Turtle', 'Reptile', 'Coral Reef', 10, 160.0),
(4, 'Clownfish', 'Fish', 'Coral Reef', 5, 0.3),
(5, 'Hammerhead Shark', 'Fish', 'Open Ocean', 70, 230.0),
(6, 'Giant Octopus', 'Mollusc', 'Seabed', 40, 25.0),
(7, 'Manta Ray', 'Fish', 'Open Ocean', 25, 1350.0),
(8, 'Starfish', 'Echinoderm', 'Seabed', 20, 0.5)""")

print("All observations:")
cur.execute("""SELECT * FROM marine_observation""")
for row in cur.fetchall():
    print(row)
print()

print("All animal groups:")
cur.execute("""SELECT animal_group FROM marine_observation""")
for row in cur.fetchall():
    print(row)
print()

print("Unique animal groups:")
cur.execute("""SELECT DISTINCT animal_group FROM marine_observation""")
for row in cur.fetchall():
    print(row)
print()

print("Number of unique animal groups:")
cur.execute("""SELECT COUNT(DISTINCT animal_group) AS unique_animal_groups FROM marine_observation""")
for row in cur.fetchall():
    print(row)
print()

print("Total observations:")
cur.execute("""SELECT COUNT(observation_id) AS total_observations FROM marine_observation""")
for row in cur.fetchall():
    print(row)
print()

print("Open Ocean observations:")
cur.execute("""SELECT COUNT(observation_id) AS open_ocean_observations FROM marine_observation WHERE habitat = 'Open Ocean'""")
for row in cur.fetchall():
    print(row)
print()

print("Total estimated weight:")
cur.execute("""SELECT SUM(estimated_weight_kg) AS total_weight_kg FROM marine_observation""")
for row in cur.fetchall():
    print(row)
print()

print("Average depth:")
cur.execute("""SELECT AVG(depth_m) AS average_depth_m FROM marine_observation""")
for row in cur.fetchall():
    print(row)
print()

print("Summary:")
cur.execute("""SELECT COUNT(observation_id) AS total_observations, COUNT(DISTINCT animal_group) AS unique_animal_groups, SUM(estimated_weight_kg) AS total_weight_kg, AVG(depth_m) AS average_depth_m FROM marine_observation""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
