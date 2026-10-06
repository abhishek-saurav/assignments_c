import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS book (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL NOT NULL,
    pages INTEGER NOT NULL,
    pub_year INTEGER NOT NULL
)""")
cur.execute("""INSERT INTO book VALUES
(1, 'Dragon Quest', 'Fantasy', 9.2, 312, 2021),
(2, 'Code Wizards', 'Sci-Fi', 8.5, 280, 2020),
(3, 'Ocean Deep', 'Adventure', 7.8, 195, 2022),
(4, 'Star Rangers', 'Sci-Fi', 9.5, 340, 2019),
(5, 'Forest Secrets', 'Fantasy', 8.1, 228, 2023),
(6, 'Robot City', 'Sci-Fi', 7.2, 260, 2021),
(7, 'Time Jumpers', 'Adventure', 8.9, 175, 2022),
(8, 'Magic Academy', 'Fantasy', 9.0, 398, 2020)""")

print("All books:")
cur.execute("""SELECT * FROM book""")
for row in cur.fetchall():
    print(row)
print()

print("Lowest rating first:")
cur.execute("""SELECT title, rating FROM book ORDER BY rating ASC""")
for row in cur.fetchall():
    print(row)
print()

print("Highest rating first:")
cur.execute("""SELECT title, rating FROM book ORDER BY rating DESC""")
for row in cur.fetchall():
    print(row)
print()

print("Genre A-Z, then highest rating first:")
cur.execute("""SELECT title, genre, rating FROM book ORDER BY genre ASC, rating DESC""")
for row in cur.fetchall():
    print(row)
print()

print("Top 3 highest-rated books:")
cur.execute("""SELECT title, rating FROM book ORDER BY rating DESC LIMIT 3""")
for row in cur.fetchall():
    print(row)
print()

print("5 oldest books:")
cur.execute("""SELECT title, pub_year FROM book ORDER BY pub_year ASC LIMIT 5""")
for row in cur.fetchall():
    print(row)
print()

print("Books per genre:")
cur.execute("""SELECT genre, COUNT(*) AS book_count FROM book GROUP BY genre""")
for row in cur.fetchall():
    print(row)
print()

print("Total pages and average rating per genre:")
cur.execute("""SELECT genre, SUM(pages) AS total_pages, AVG(rating) AS avg_rating FROM book GROUP BY genre""")
for row in cur.fetchall():
    print(row)
print()

print("Genres with more than 2 books:")
cur.execute("""SELECT genre, COUNT(*) AS book_count FROM book GROUP BY genre HAVING COUNT(*) > 2""")
for row in cur.fetchall():
    print(row)
print()

print("Genres with an average rating of at least 8.5:")
cur.execute("""SELECT genre, AVG(rating) AS avg_rating FROM book GROUP BY genre HAVING AVG(rating) >= 8.5""")
for row in cur.fetchall():
    print(row)
print()

conn.close()
