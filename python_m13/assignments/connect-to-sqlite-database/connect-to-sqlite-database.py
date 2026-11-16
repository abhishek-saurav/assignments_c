import sqlite3
import pandas as pd

database = ':memory:'
conn = sqlite3.connect(database)
print('Connected to the St. Alberts database')

conn.execute("""CREATE TABLE photo (
    photo_id INTEGER PRIMARY KEY,
    title TEXT,
    photographer TEXT
)""")
conn.execute("INSERT INTO photo VALUES (1, 'Sunrise at the lake', 'Abhishek')")
conn.execute("INSERT INTO photo VALUES (2, 'Old church door', 'Abhishek')")
conn.commit()

tables = pd.read_sql("""SELECT *
    FROM sqlite_master
    WHERE type='table';""", conn)
print(tables)

photos = pd.read_sql("""SELECT *
    FROM photo;""", conn)
print(photos)

conn.close()
