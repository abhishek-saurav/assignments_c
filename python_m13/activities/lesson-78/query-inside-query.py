import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

conn.execute("CREATE TABLE song (song_id INTEGER PRIMARY KEY, song_name TEXT NOT NULL, style TEXT NOT NULL, minutes INTEGER NOT NULL)")
conn.execute("CREATE TABLE chord (chord_id INTEGER PRIMARY KEY, song_id INTEGER NOT NULL, chord_name TEXT NOT NULL, strums INTEGER NOT NULL)")
conn.executemany("INSERT INTO song VALUES (?, ?, ?, ?)", [
    (1, 'Wonderwall', 'Pop', 4),
    (2, 'Hotel California', 'Rock', 6),
    (3, 'Blackbird', 'Folk', 2),
    (4, 'Hallelujah', 'Folk', 4),
])
conn.executemany("INSERT INTO chord VALUES (?, ?, ?, ?)", [
    (1, 1, 'Em', 8),
    (2, 1, 'G', 8),
    (3, 2, 'Bm', 4),
    (4, 3, 'G', 6),
    (5, 4, 'C', 10),
])
conn.commit()

busy_songs = pd.read_sql("SELECT song_name AS title, style AS genre "
                         "FROM song "
                         "WHERE song_id IN ("
                         "SELECT song_id FROM chord WHERE strums > 6"
                         ")", conn)
print("Subquery with IN -- songs with a chord strummed more than 6 times:")
print(busy_songs)
print()

shortest = pd.read_sql("SELECT song_name AS title, minutes AS length "
                       "FROM song "
                       "WHERE minutes = (SELECT MIN(minutes) FROM song)", conn)
print("Subquery with = -- the shortest song:")
print(shortest)

conn.close()
