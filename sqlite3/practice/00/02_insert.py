import sqlite3

db_filename = 'test.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    conn.execute("Insert into test00 (data) values ('hello123')")
    conn.commit()
