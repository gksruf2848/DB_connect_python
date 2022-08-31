#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
    RUN:
        $ uvicorn HanlimSqlite_fastApi:app --reload
"""

#end_pymotw_header

# layout_07_server.py

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Set, Union
import json
import sqlite3

app = FastAPI()


# --- DB ---
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


# --- Req Classes ---
class SettlementInfoWithdraw(BaseModel):
    bank_code: str
    settlement_account_num: str
    settlement_amt: float

class DepositRequirementChangeDetails(BaseModel):
    deposit_requirement_type: str
    increase_amt: float
    decrease_amt: float


# --- 004 : POST
class Req004Items(BaseModel):
    code: str = 'CD001' #code
    account_num: str = 'ABCD1234'
    currency_code: int = 123
    tran_amt: int = 20000
    withdraw_reason_code: str = 'A1'
    settlement_info_withdraw_cnt: int = 2
    settlement_info_withdraw: Union[List[SettlementInfoWithdraw], None] = [
        {
            'bank_code': 'B1',
            'settlement_account_num': 'BBBB2222',
            'settlement_amt': 300.00
        },{
            'bank_code': 'C1',
            'settlement_account_num': 'DDDD1111',
            'settlement_amt': 200.00
        }
    ]
    consignment_guarantee : float = 123.123
    deposit_requirement_change_details_cnt : int = 123
    deposit_requirement_change_details : Union[List[DepositRequirementChangeDetails], None] = [
        {
            'deposit_requirement_type': 'B2',
            'increase_amt': 123.12,
            'decrease_amt': 123.12
        }, {
            'deposit_requirement_type': 'C2',
            'increase_amt': 111.11,
            'decrease_amt': 111.11
        }
    ]
    optr_email_yn: str = 'Y'
    optr_email_address: str = '4455qqq@naver.com'
    apvr_email_yn: str = 'Y'
    apvr_email_address: str = 'gksruf2848@naver.com'
    optr_sms_yn: str = 'Y'
    optr_mobile_num: int = '01054149634'
    apvr_sms_yn: str = 'Y'
    apvr_mobile_num: int = '01058446024'
    

@app.post('/deposit/invr_dpsa/transfer/withdraw')
async def postIndex(reqItems: Req004Items):
    print('REQ >>>', reqItems)
    dic = json.loads(res_004)
    dic['rsp_code'] = reqItems.code
    return dic
