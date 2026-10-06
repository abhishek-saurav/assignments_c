import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS PRODUCT""")
cur.execute("""CREATE TABLE PRODUCT (
    PRO_ID TEXT PRIMARY KEY,
    PRO_NAME TEXT NOT NULL,
    PRO_PRICE INTEGER NOT NULL,
    PRO_COM TEXT NOT NULL
)""")
cur.execute("""INSERT INTO PRODUCT (PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM) VALUES
('101', 'MOTHER BOARD', 3200, 'TECHPRO'),
('102', 'KEY BOARD', 450, 'KEYMAX'),
('103', 'ZIP DRIVE', 250, 'DATAFIX'),
('104', 'SPEAKER', 550, 'SOUNDCO'),
('105', 'MONITOR', 5000, 'VIEWTECH'),
('106', 'DVD DRIVE', 900, 'DATAFIX'),
('107', 'CD DRIVE', 800, 'DATAFIX'),
('108', 'PRINTER', 2600, 'PRINTPLUS'),
('109', 'REFILL CARTRIDGE', 350, 'PRINTPLUS'),
('110', 'MOUSE', 250, 'KEYMAX')""")

print("All products:")
cur.execute("""SELECT * FROM PRODUCT""")
for row in cur.fetchall():
    print(row)
print()

print("Priced below 1000 and made by DATAFIX:")
cur.execute("""SELECT * FROM PRODUCT WHERE PRO_PRICE < 1000 AND PRO_COM = 'DATAFIX'""")
for row in cur.fetchall():
    print(row)
print()

print("Made by KEYMAX or priced above 3000:")
cur.execute("""SELECT * FROM PRODUCT WHERE PRO_COM = 'KEYMAX' OR PRO_PRICE > 3000""")
for row in cur.fetchall():
    print(row)
print()

print("Under 1000 and made by DATAFIX or KEYMAX:")
cur.execute("""SELECT * FROM PRODUCT WHERE PRO_PRICE < 1000 AND (PRO_COM = 'DATAFIX' OR PRO_COM = 'KEYMAX')""")
for row in cur.fetchall():
    print(row)
print()

print("Names that start with M:")
cur.execute("""SELECT * FROM PRODUCT WHERE PRO_NAME LIKE 'M%'""")
for row in cur.fetchall():
    print(row)
print()

print("Names that end with DRIVE:")
cur.execute("""SELECT * FROM PRODUCT WHERE PRO_NAME LIKE '%DRIVE'""")
for row in cur.fetchall():
    print(row)
print()

print("Names that contain PRINT:")
cur.execute("""SELECT * FROM PRODUCT WHERE PRO_NAME LIKE '%PRINT%'""")
for row in cur.fetchall():
    print(row)
print()

print("Lowest price:")
cur.execute("""SELECT PRO_NAME, PRO_PRICE FROM PRODUCT WHERE PRO_PRICE = (SELECT MIN(PRO_PRICE) FROM PRODUCT)""")
for row in cur.fetchall():
    print(row)
print()

print("Highest price:")
cur.execute("""SELECT PRO_NAME, PRO_PRICE FROM PRODUCT WHERE PRO_PRICE = (SELECT MAX(PRO_PRICE) FROM PRODUCT)""")
for row in cur.fetchall():
    print(row)
print()

cur.execute("""UPDATE PRODUCT SET PRO_PRICE = 600 WHERE PRO_ID = '104'""")

print("After updating the Speaker price:")
cur.execute("""SELECT * FROM PRODUCT WHERE PRO_ID = '104'""")
for row in cur.fetchall():
    print(row)
print()

cur.execute("""DELETE FROM PRODUCT WHERE PRO_ID = '103'""")

print("After deleting ZIP DRIVE:")
cur.execute("""SELECT * FROM PRODUCT""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
