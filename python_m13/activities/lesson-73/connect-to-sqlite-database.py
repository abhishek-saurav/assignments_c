import sqlite3
import pandas as pd

database = ':memory:'
conn = sqlite3.connect(database)
print('Opened database successfully')

conn.execute("""CREATE TABLE chess_player (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT,
    rating INTEGER
)""")
conn.commit()

tables = pd.read_sql("""SELECT *
    FROM sqlite_master
    WHERE type='table';""", conn)
print(tables)

conn.close()
