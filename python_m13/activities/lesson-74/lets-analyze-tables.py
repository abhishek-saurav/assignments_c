import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE chess_player (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT,
    school TEXT,
    rating INTEGER
);
CREATE TABLE chess_match (
    match_id INTEGER PRIMARY KEY,
    winner_id INTEGER,
    moves INTEGER
);
INSERT INTO chess_player VALUES
    (1,'Abhishek','St. Alberts',1450),
    (2,'Rohan','St. Alberts',1320),
    (3,'Meera','St. Marys',1510),
    (4,'Kabir','St. Marys',1275);
INSERT INTO chess_match VALUES
    (1,1,34),(2,3,41),(3,1,28),(4,2,52);
""")
conn.commit()
print('Database ready!')

tables = pd.read_sql("""SELECT *
    FROM sqlite_master
    WHERE type='table';""", conn)
print(tables)

players = pd.read_sql("""SELECT *
    FROM chess_player;""", conn)
print(players)
print('Rows and columns:', players.shape)

names = pd.read_sql("""SELECT player_id, player_name
    FROM chess_player;""", conn)
print(names)

matches = pd.read_sql("""SELECT match_id, winner_id
    FROM chess_match;""", conn)
print(matches)

conn.close()
