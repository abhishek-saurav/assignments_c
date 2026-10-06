import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS STUDENT (
    ROLL_NO TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
)""")
cur.execute("""INSERT INTO STUDENT (ROLL_NO, NAME, ADDRESS, PHONE, AGE) VALUES
('1', 'RAM', 'DELHI', '******', 18),
('2', 'RAMESH', 'GURGAON', '******', 18),
('3', 'SUJIT', 'ROHTAK', '******', 20),
('4', 'SURESH', 'DELHI', '******', 18),
('5', 'AMAN', 'ROHTAK', '******', 20),
('6', 'HARSH', 'GURGAON', '******', 18)""")

print("All students:")
cur.execute("""SELECT * FROM STUDENT""")
for row in cur.fetchall():
    print(row)
print()

print("Students aged 18 who live in Delhi:")
cur.execute("""SELECT * FROM STUDENT WHERE AGE = 18 AND ADDRESS = 'DELHI'""")
for row in cur.fetchall():
    print(row)
print()

print("Students aged 18 named Ram:")
cur.execute("""SELECT * FROM STUDENT WHERE AGE = 18 AND NAME = 'RAM'""")
for row in cur.fetchall():
    print(row)
print()

print("Students named Ram or Sujit:")
cur.execute("""SELECT * FROM STUDENT WHERE NAME = 'RAM' OR NAME = 'SUJIT'""")
for row in cur.fetchall():
    print(row)
print()

print("Students named Ram or aged 20:")
cur.execute("""SELECT * FROM STUDENT WHERE NAME = 'RAM' OR AGE = 20""")
for row in cur.fetchall():
    print(row)
print()

print("Students aged 18 named Ram or Ramesh:")
cur.execute("""SELECT * FROM STUDENT WHERE AGE = 18 AND (NAME = 'RAM' OR NAME = 'RAMESH')""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
