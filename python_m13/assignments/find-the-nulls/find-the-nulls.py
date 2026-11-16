import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

conn.execute("""
CREATE TABLE Camera (
    Camera_Id INTEGER PRIMARY KEY,
    Camera_Name TEXT NOT NULL UNIQUE,
    Brand TEXT NOT NULL,
    Price INTEGER,
    In_Use TEXT DEFAULT 'Yes'
);
""")
conn.execute("INSERT INTO Camera VALUES (1, 'D3500', 'Nikon', 38000, 'Yes');")
conn.execute("INSERT INTO Camera VALUES (2, 'EOS 1500D', 'Canon', 32000, 'Yes');")
conn.execute("INSERT INTO Camera VALUES (3, 'A6000', 'Sony', 55000, 'No');")
conn.execute("INSERT INTO Camera (Camera_Id, Camera_Name, Brand) VALUES (4, 'Z50', 'Nikon');")
conn.execute("INSERT INTO Camera (Camera_Id, Camera_Name, Brand) VALUES (5, 'M50', 'Canon');")
conn.commit()

all_cameras = pd.read_sql("""SELECT Camera_Name, Brand, Price, In_Use
    FROM Camera;""", conn)
print(all_cameras)

missing = pd.read_sql("""SELECT Camera_Name FROM Camera
    WHERE Price IS NULL;""", conn)
print("Cameras with no price:")
print(missing)

has_price = pd.read_sql("""SELECT Camera_Name, Price FROM Camera
    WHERE Price IS NOT NULL;""", conn)
print("Cameras with a price:")
print(has_price)

conn.close()
