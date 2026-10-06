import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE supplier (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
)""")
cur.execute("""INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES
('S1', 'Smith', 20, 'London'),
('S2', 'Jones', 10, 'Paris'),
('S3', 'Blake', 30, 'Paris'),
('S4', 'Clarke', 20, 'London'),
('S5', 'Adams', 30, 'Athens')""")

print("All suppliers:")
cur.execute("""SELECT * FROM supplier""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
