import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE PRODUCT (
    PRO_ID TEXT PRIMARY KEY,
    PRO_NAME TEXT NOT NULL,
    PRO_PRICE INTEGER NOT NULL,
    PRO_COM TEXT NOT NULL
)""")
cur.execute("""INSERT INTO PRODUCT (PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM) VALUES
('201', 'CAMERA BODY', 45000, 'LENSKART'),
('202', 'LENS 50MM', 12000, 'LENSKART'),
('203', 'TRIPOD', 2500, 'STEADYCO'),
('204', 'FLASH LIGHT', 6000, 'BRIGHTCO'),
('205', 'MEMORY CARD', 800, 'DATAFIX'),
('206', 'CAMERA BAG', 3500, 'STEADYCO'),
('207', 'LENS CAP', 300, 'LENSKART'),
('208', 'LENS CLEANER', 300, 'CLEANPRO')""")

print("All products:")
cur.execute("""SELECT * FROM PRODUCT""")
for row in cur.fetchall():
    print(row)
print()

print("Cheapest products:")
cur.execute("""SELECT PRO_NAME, PRO_PRICE FROM PRODUCT WHERE PRO_PRICE = (SELECT MIN(PRO_PRICE) FROM PRODUCT)""")
for row in cur.fetchall():
    print(row)
print()

print("Most expensive product:")
cur.execute("""SELECT PRO_NAME, PRO_PRICE FROM PRODUCT WHERE PRO_PRICE = (SELECT MAX(PRO_PRICE) FROM PRODUCT)""")
for row in cur.fetchall():
    print(row)
print()

print("Names that start with L:")
cur.execute("""SELECT PRO_NAME, PRO_PRICE FROM PRODUCT WHERE PRO_NAME LIKE 'L%'""")
for row in cur.fetchall():
    print(row)
print()

print("Names that contain CAMERA:")
cur.execute("""SELECT PRO_NAME, PRO_PRICE FROM PRODUCT WHERE PRO_NAME LIKE '%CAMERA%'""")
for row in cur.fetchall():
    print(row)
print()

print("LENSKART products under 20000:")
cur.execute("""SELECT PRO_NAME, PRO_PRICE FROM PRODUCT WHERE PRO_COM = 'LENSKART' AND PRO_PRICE < 20000""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
