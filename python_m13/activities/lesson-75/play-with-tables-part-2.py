import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE photo (
    photo_id INTEGER PRIMARY KEY,
    title TEXT,
    category TEXT,
    year INTEGER,
    rating REAL,
    likes INTEGER
);
INSERT INTO photo VALUES
    (1,'Sunrise at the lake','Landscape',2021,8.5,120),
    (2,'Old church door','Architecture',2022,7.8,85),
    (3,'Chess club finals','Portrait',2023,9.1,210),
    (4,'Monsoon street','Street',2022,8.2,95),
    (5,'Hills at dusk','Landscape',2023,8.9,160),
    (6,'Guitar on the stage','Portrait',2021,7.5,70),
    (7,'Market morning','Street',2023,8.0,110);
""")
conn.commit()

categories = pd.read_sql("""SELECT DISTINCT(category)
    FROM photo;""", conn)
print(categories)

best_first = pd.read_sql("""SELECT title, category, rating
    FROM photo
    ORDER BY rating DESC;""", conn)
print(best_first)

oldest_first = pd.read_sql("""SELECT title, year
    FROM photo
    ORDER BY year;""", conn)
print(oldest_first)

street_count = pd.read_sql("""SELECT COUNT(photo_id)
    FROM photo
    WHERE category == 'Street';""", conn)
print(street_count)

landscape_likes = pd.read_sql("""SELECT SUM(likes)
    FROM photo
    WHERE category == 'Landscape';""", conn)
print(landscape_likes)

avg_rating = pd.read_sql("""SELECT AVG(rating)
    FROM photo;""", conn)
print(avg_rating)

photos_per_category = pd.read_sql("""SELECT category, COUNT(photo_id)
    FROM photo
    GROUP BY category;""", conn)
print(photos_per_category)

avg_per_category = pd.read_sql("""SELECT category, AVG(rating)
    FROM photo
    GROUP BY category
    ORDER BY AVG(rating) DESC;""", conn)
print(avg_per_category)

conn.close()
