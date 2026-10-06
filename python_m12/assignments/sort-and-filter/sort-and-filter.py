import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS community_activity (
    activity_id INTEGER PRIMARY KEY,
    activity_name TEXT NOT NULL,
    activity_type TEXT NOT NULL,
    day TEXT NOT NULL,
    participants INTEGER NOT NULL,
    duration_mins INTEGER NOT NULL
)""")
cur.execute("""INSERT INTO community_activity VALUES
(1, 'Yoga Class', 'Wellness', 'Monday', 18, 60),
(2, 'Art Workshop', 'Creative', 'Tuesday', 12, 90),
(3, 'Chess Club', 'Games', 'Wednesday', 16, 75),
(4, 'Dance Practice', 'Wellness', 'Thursday', 20, 60),
(5, 'Coding Club', 'Learning', 'Friday', 14, 90),
(6, 'Book Circle', 'Learning', 'Saturday', 10, 60),
(7, 'Painting Club', 'Creative', 'Saturday', 15, 75),
(8, 'Football Practice', 'Sports', 'Sunday', 22, 90),
(9, 'Meditation Hour', 'Wellness', 'Sunday', 13, 45)""")

print("All activities:")
cur.execute("""SELECT * FROM community_activity""")
for row in cur.fetchall():
    print(row)
print()

print("Fewest participants first:")
cur.execute("""SELECT activity_name, participants FROM community_activity ORDER BY participants ASC""")
for row in cur.fetchall():
    print(row)
print()

print("Most participants first:")
cur.execute("""SELECT activity_name, participants FROM community_activity ORDER BY participants DESC""")
for row in cur.fetchall():
    print(row)
print()

print("Type A-Z, then most participants first:")
cur.execute("""SELECT activity_name, activity_type, participants FROM community_activity ORDER BY activity_type ASC, participants DESC""")
for row in cur.fetchall():
    print(row)
print()

print("Top 3 activities by participants:")
cur.execute("""SELECT activity_name, participants FROM community_activity ORDER BY participants DESC LIMIT 3""")
for row in cur.fetchall():
    print(row)
print()

print("5 shortest activities:")
cur.execute("""SELECT activity_name, duration_mins FROM community_activity ORDER BY duration_mins ASC LIMIT 5""")
for row in cur.fetchall():
    print(row)
print()

print("Activities per type:")
cur.execute("""SELECT activity_type, COUNT(*) AS activity_count FROM community_activity GROUP BY activity_type""")
for row in cur.fetchall():
    print(row)
print()

print("Total participants and average duration per type:")
cur.execute("""SELECT activity_type, SUM(participants) AS total_participants, AVG(duration_mins) AS avg_duration FROM community_activity GROUP BY activity_type""")
for row in cur.fetchall():
    print(row)
print()

print("Types with more than 2 activities:")
cur.execute("""SELECT activity_type, COUNT(*) AS activity_count FROM community_activity GROUP BY activity_type HAVING COUNT(*) > 2""")
for row in cur.fetchall():
    print(row)
print()

print("Types with an average of at least 15 participants:")
cur.execute("""SELECT activity_type, AVG(participants) AS avg_participants FROM community_activity GROUP BY activity_type HAVING AVG(participants) >= 15""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
