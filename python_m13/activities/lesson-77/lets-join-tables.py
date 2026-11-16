import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

conn.execute("""CREATE TABLE club (
    club_id INTEGER PRIMARY KEY,
    club_name TEXT NOT NULL UNIQUE
)""")
conn.execute("""CREATE TABLE member (
    member_id INTEGER PRIMARY KEY,
    member_name TEXT NOT NULL,
    club_id INTEGER
)""")
conn.executemany("INSERT INTO club VALUES (?, ?)", [
    (1, 'Chess Club'),
    (2, 'Photography Club'),
    (3, 'Guitar Club'),
    (4, 'Coding Club'),
])
conn.executemany("INSERT INTO member VALUES (?, ?, ?)", [
    (1, 'Abhishek', 1),
    (2, 'Rohan', 1),
    (3, 'Meera', 2),
    (4, 'Kabir', 3),
    (5, 'Anaya', 3),
])
conn.commit()

clubs = pd.read_sql("SELECT * FROM club", conn)
members = pd.read_sql("SELECT * FROM member", conn)
print("Club table:")
print(clubs)
print()
print("Member table:")
print(members)
print()

inner = pd.read_sql("SELECT club.club_name, member.member_name "
                    "FROM club INNER JOIN member ON club.club_id = member.club_id", conn)
print("INNER JOIN - clubs matched with their members:")
print(inner)
print()

left = pd.read_sql("SELECT club.club_name, member.member_name "
                   "FROM club LEFT JOIN member ON club.club_id = member.club_id", conn)
print("LEFT JOIN - all clubs, NULL where no member found:")
print(left)

conn.close()
