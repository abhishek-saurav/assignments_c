import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

conn.execute("CREATE TABLE camera (camera_id INTEGER PRIMARY KEY, camera_name TEXT NOT NULL, brand TEXT NOT NULL, price INTEGER NOT NULL)")
conn.execute("CREATE TABLE lens (lens_id INTEGER PRIMARY KEY, camera_id INTEGER NOT NULL, lens_name TEXT NOT NULL, focal_mm INTEGER NOT NULL)")
conn.executemany("INSERT INTO camera VALUES (?, ?, ?, ?)", [
    (1, 'D3500', 'Nikon', 38000),
    (2, 'EOS 1500D', 'Canon', 32000),
    (3, 'A6000', 'Sony', 55000),
    (4, 'Z50', 'Nikon', 85000),
])
conn.executemany("INSERT INTO lens VALUES (?, ?, ?, ?)", [
    (1, 1, 'Kit lens', 55),
    (2, 1, 'Prime lens', 50),
    (3, 2, 'Telephoto lens', 200),
    (4, 3, 'Wide lens', 16),
    (5, 4, 'Zoom lens', 135),
])
conn.commit()

long_lens = pd.read_sql("SELECT camera_name AS camera, brand AS maker "
                        "FROM camera "
                        "WHERE camera_id IN ("
                        "SELECT camera_id FROM lens WHERE focal_mm > 100"
                        ")", conn)
print("Subquery with IN -- cameras with a lens longer than 100mm:")
print(long_lens)
print()

cheapest = pd.read_sql("SELECT camera_name AS camera, price AS cost "
                       "FROM camera "
                       "WHERE price = (SELECT MIN(price) FROM camera)", conn)
print("Subquery with = -- the cheapest camera:")
print(cheapest)

conn.close()
