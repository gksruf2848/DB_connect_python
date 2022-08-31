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

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    conn.execute("Insert into tbl_004 (rsp_code, rsp_msg, tran_idn_num) values ('CODE', '응답메시지입니다', 'BA23')")
    conn.commit()

    cursor.execute("""
    select * from tbl_004 where id = 1
    """)
    id, rsp_code, rsp_msg, tran_idn_num = cursor.fetchone()

    res_004 = '{"id":' + str(id) + ',"rsp_code":"' + rsp_code + '", "rsp_msg":"' + rsp_msg + '", "tran_idn_num":"' + tran_idn_num + '"}'
    print(res_004)