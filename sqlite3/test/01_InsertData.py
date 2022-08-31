import sqlite3

db_filename = 'hanlim.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from tbl_004 where 1 = 1
    """)
    lstRes = []
    for id, rsp_code, rsp_msg, tran_idn_num in cursor.fetchall():
        #print(id, rsp_code, rsp_msg, tran_idn_num)
        dic = {}
        dic["id"] = id
        dic["rsp_code"] = rsp_code
        dic["rsp_msg"] = rsp_msg
        dic["tran_idn_num"] = tran_idn_num

        #print(dic)
        lstRes.append(dic)
    
    print(lstRes)