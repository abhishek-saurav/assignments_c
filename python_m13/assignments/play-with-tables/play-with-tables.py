import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE guitar_song (
    song_id INTEGER PRIMARY KEY,
    song_name TEXT,
    style TEXT,
    minutes INTEGER
);
INSERT INTO guitar_song VALUES
    (1,'Wonderwall','Pop',4),
    (2,'Hotel California','Rock',6),
    (3,'Blackbird','Folk',2),
    (4,'Wish You Were Here','Rock',5),
    (5,'Hallelujah','Folk',4),
    (6,'Tears in Heaven','Pop',5);
""")
conn.commit()

songs = pd.read_sql("""SELECT *
    FROM guitar_song;""", conn)
print(songs)

names = pd.read_sql("""SELECT song_id, song_name
    FROM guitar_song;""", conn)
print(names)

rock = pd.read_sql("""SELECT *
    FROM guitar_song
    WHERE style == 'Rock';""", conn)
print(rock)

short_folk = pd.read_sql("""SELECT *
    FROM guitar_song
    WHERE style == 'Folk' AND minutes IN (2, 3);""", conn)
print(short_folk)

w_songs = pd.read_sql("""SELECT *
    FROM guitar_song
    WHERE song_name LIKE 'W%';""", conn)
print(w_songs)

lengths = pd.read_sql("""SELECT MIN(minutes), MAX(minutes)
    FROM guitar_song;""", conn)
print(lengths)

conn.close()
