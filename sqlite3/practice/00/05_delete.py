import sqlite3

db_filename = 'test.db'
query = "delete from test00 where id = 2"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()