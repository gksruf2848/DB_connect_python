# Creating a table.

import sqlite3

db_filename = 'hanlim.db'

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    conn.execute("""
    create table if not exists obj (
        id    integer primary key autoincrement not null,
        data  text
    )""")
    