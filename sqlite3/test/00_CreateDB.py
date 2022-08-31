import sqlite3

db_filename = 'hanlim.db'

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    conn.execute("""
    create table if not exists tbl_004 (
        id              integer primary key autoincrement not null,
        rsp_code        text,
        rsp_msg         text,
        tran_idn_num    text
    )""")
