import sqlite3

db_filename = 'hanlim.db'
query = "update obj set data = 'ABC' where id = 1"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()