import sqlite3

db_filename = 'hanlim.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute("""
    select * from obj
    """)

    #cursor.fetchone()
    for (id, data) in cursor.fetchall():
        print(id, data)