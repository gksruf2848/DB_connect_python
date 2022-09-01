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

# HanlimSqlite_fastApi.py

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Set, Union
import json
import sqlite3

app = FastAPI()


# --- DB ---
db_filename = 'hanlim.db'
    

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
class ReqImsiItems(BaseModel):
    # id: int = 1
    rsp_code: str = 'GJWY'
    rsp_msg: str = '응답'
    tran_idn_num: str = 'AA'

class ReqUpdateItems(BaseModel):
    id: int = 1
    rsp_code: str = 'GJWY'
    rsp_msg: str = '응답'
    tran_idn_num: str = 'AA'


@app.post('/hanlim/update')
async def insert(reqItems: ReqImsiItems):
    print('REQ >>>', reqItems)
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        # update obj set data = 'ABC' where id = 1
        cursor.execute("update tbl_004 set date = '" + reqItems.rsp_code + "' where id = " + reqItems.id)
        
        # (rsp_code, rsp_msg, tran_idn_num) values ('" + reqItems.rsp_code + "', '" + reqItems.rsp_msg + "', ' " + reqItems.tran_idn_num + "')")
        cursor.execute("select * from tbl_004 where id = last_insert_rowid()")
        conn.commit()
        id, rsp_code, rsp_msg, tran_idn_num = cursor.fetchone()
        # dic = {}
        dic = dict()
        dic["id"] = id
        dic["rsp_code"] = rsp_code
        dic["rsp_msg"] = rsp_msg
        dic["tran_idn_num"] = tran_idn_num
    return dic


@app.post('/hanlim/insert')
async def insert(reqItems: ReqImsiItems):
    print('REQ >>>', reqItems)
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute("insert into tbl_004 (rsp_code, rsp_msg, tran_idn_num) values ('" + reqItems.rsp_code + "', '" + reqItems.rsp_msg + "', ' " + reqItems.tran_idn_num + "')")
        cursor.execute("select * from tbl_004 where id = last_insert_rowid()")
        conn.commit()
        id, rsp_code, rsp_msg, tran_idn_num = cursor.fetchone()
        # dic = {}
        dic = dict()
        dic["id"] = id
        dic["rsp_code"] = rsp_code
        dic["rsp_msg"] = rsp_msg
        dic["tran_idn_num"] = tran_idn_num
    return dic


@app.get('/hanlim/selectone')
async def selectOne(id: int):
    print('REQ >>> id = ', id)
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute("select * from tbl_004 where id = " + str(id))
        id, rsp_code, rsp_msg, tran_idn_num = cursor.fetchone()
        # dic = {}
        dic = dict()
        dic["id"] = id
        dic["rsp_code"] = rsp_code
        dic["rsp_msg"] = rsp_msg
        dic["tran_idn_num"] = tran_idn_num
    return dic


@app.post('/hanlim/selectall')
async def selectAll(reqItems: ReqImsiItems):
    print('REQ >>>', reqItems)
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()

        cursor.execute("select * from tbl_004 where 1 = 1")
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

    #dic = json.loads(lstRes)
    # dic['rsp_code'] = reqItems.code
    return lstRes