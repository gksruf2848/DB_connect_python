import sqlite3

db_filename = 'test.db'
query = "update test00 set name = 'ABC', age = 10 where id = 3"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()