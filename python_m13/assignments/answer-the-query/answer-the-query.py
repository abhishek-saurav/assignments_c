import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE coding_project (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    language TEXT,
    lines_of_code INTEGER,
    hours INTEGER
);
INSERT INTO coding_project VALUES
    (1,'Quiz game','Python',120,6),
    (2,'Chess clock','Python',200,10),
    (3,'School website','HTML',350,15),
    (4,'Photo gallery','HTML',280,12),
    (5,'Guitar tuner','Python',150,8),
    (6,'Score tracker','JavaScript',180,9);
""")
conn.commit()

languages = pd.read_sql("""SELECT DISTINCT(language)
    FROM coding_project;""", conn)
print("Languages used:")
print(languages)

longest_first = pd.read_sql("""SELECT project_name, lines_of_code
    FROM coding_project
    ORDER BY lines_of_code DESC;""", conn)
print("Projects, longest first:")
print(longest_first)

python_count = pd.read_sql("""SELECT COUNT(project_id)
    FROM coding_project
    WHERE language == 'Python';""", conn)
print("Number of Python projects:")
print(python_count)

total_hours = pd.read_sql("""SELECT SUM(hours)
    FROM coding_project;""", conn)
print("Total hours spent:")
print(total_hours)

avg_lines = pd.read_sql("""SELECT AVG(lines_of_code)
    FROM coding_project;""", conn)
print("Average lines of code:")
print(avg_lines)

per_language = pd.read_sql("""SELECT language, COUNT(project_id)
    FROM coding_project
    GROUP BY language;""", conn)
print("Projects per language:")
print(per_language)

conn.close()
