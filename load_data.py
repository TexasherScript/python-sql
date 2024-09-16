import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="workshopdb",
    user="user",
    password="password"
)

df = pd.read_csv('data/your_dataset.csv')

# Create table and insert data
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS dataset_table (
    column1 TEXT,
    column2 INTEGER,
    ...
);
""")

for index, row in df.iterrows():
    cur.execute("""
    INSERT INTO dataset_table (column1, column2, ...) VALUES (%s, %s, ...);
    """, (row['column1'], row['column2'], ...))

conn.commit()
cur.close()
conn.close()
