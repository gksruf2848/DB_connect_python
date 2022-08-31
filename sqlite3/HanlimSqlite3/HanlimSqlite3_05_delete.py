import sqlite3

db_filename = 'hanlim.db'
query = "delete from obj where id = 2"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()