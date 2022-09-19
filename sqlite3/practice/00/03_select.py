import sqlite3

db_filename = 'test.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute("""
    select * from test00
    """)

    #cursor.fetchone()
    for (id, name, age) in cursor.fetchall():
        print(id, name, age)