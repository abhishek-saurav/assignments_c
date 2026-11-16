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
INSERT INTO chess_player VALUES
    (1,'Abhishek','St. Alberts',1450),
    (2,'Rohan','St. Alberts',1320),
    (3,'Meera','St. Marys',1510),
    (4,'Kabir','St. Marys',1275),
    (5,'Anaya','St. Alberts',1390),
    (6,'Aditya','St. Johns',1480);
""")
conn.commit()

st_alberts = pd.read_sql("""SELECT *
    FROM chess_player
    WHERE school == 'St. Alberts';""", conn)
print(st_alberts)

strong_players = pd.read_sql("""SELECT *
    FROM chess_player
    WHERE school == 'St. Alberts' AND rating IN (1450, 1390);""", conn)
print(strong_players)

a_players = pd.read_sql("""SELECT *
    FROM chess_player
    WHERE player_name LIKE 'A%';""", conn)
print(a_players)

marys = pd.read_sql("""SELECT *
    FROM chess_player
    WHERE school LIKE '%Marys';""", conn)
print(marys)

ratings = pd.read_sql("""SELECT MIN(rating), MAX(rating)
    FROM chess_player;""", conn)
print(ratings)

conn.close()
