import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

conn.execute("CREATE TABLE song (song_id INTEGER PRIMARY KEY, song_name TEXT NOT NULL, style TEXT NOT NULL, minutes INTEGER NOT NULL)")
conn.execute("CREATE TABLE chord (chord_id INTEGER PRIMARY KEY, song_id INTEGER NOT NULL, chord_name TEXT NOT NULL, strums INTEGER NOT NULL)")
conn.executemany("INSERT INTO song VALUES (?, ?, ?, ?)", [
    (1, 'Wonderwall', 'Pop', 4),
    (2, 'Hotel California', 'Rock', 6),
    (3, 'Blackbird', 'Folk', 2),
])
conn.executemany("INSERT INTO chord VALUES (?, ?, ?, ?)", [
    (1, 1, 'Em', 8),
    (2, 1, 'G', 8),
    (3, 2, 'Bm', 4),
    (4, 3, 'G', 6),
])
conn.commit()

col_alias = pd.read_sql("SELECT song_name AS title, style AS genre, minutes AS length "
                        "FROM song", conn)
print("Column aliases -- title, genre, length:")
print(col_alias)
print()

tbl_alias = pd.read_sql("SELECT s.song_name AS title, c.chord_name, c.strums "
                        "FROM song AS s "
                        "INNER JOIN chord AS c "
                        "ON s.song_id = c.song_id", conn)
print("Table aliases -- s for song, c for chord:")
print(tbl_alias)

conn.close()
