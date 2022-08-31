import sqlite3

db_filename = 'hanlim.db'

with sqlite3.connect(db_file_name) as conn:
    cursor = conn.cursor()
    conn.execute("Insert into obj (data) values ('aaaa111')")
    conn.execute("Insert into obj (data) values ('bbbb222')")
    conn.commit()
