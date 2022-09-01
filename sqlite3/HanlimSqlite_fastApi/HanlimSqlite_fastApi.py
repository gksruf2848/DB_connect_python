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
import os

app = FastAPI()


# --- DB ---
db_filename = 'hanlim.db'
    

# --- Req Classes ---
class ReqImsiItems(BaseModel):
    # id: int = 1
    rsp_code: str = 'ABCD'
    rsp_msg: str = '응답응답'
    tran_idn_num: str = 'AA'

class ReqUpdateItems(BaseModel):
    id: int = 1
    rsp_code: str = 'GJWY'
    rsp_msg: str = '응답'
    tran_idn_num: str = 'BB'


# --- CREATE DB : GET
@app.get('/hanlim/createdb')
async def createdb():
    sqlite3.connect(db_filename)
    return {'result':'SUCCESS!'}


# --- CREATE TABLE : GET
@app.get('/hanlim/createtbl')
async def createtbl():
    with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
        conn.execute("""
        create table if not exists tbl_name (
            id              integer primary key autoincrement not null,
            rsp_code        text,
            rsp_msg         text,
            tran_idn_num    text 
        )""")
    return {'result':'SUCCESS!'}


# --- INSERT : POST
@app.post('/hanlim/insert')
async def insert(reqItems: ReqImsiItems):
    print('REQ >>>', reqItems)
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute("insert into tbl_name (rsp_code, rsp_msg, tran_idn_num) values ('" + reqItems.rsp_code + "', '" + reqItems.rsp_msg + "', ' " + reqItems.tran_idn_num + "')")
        cursor.execute("select * from tbl_name where id = last_insert_rowid()")
        conn.commit()
        id, rsp_code, rsp_msg, tran_idn_num = cursor.fetchone()
        # dic = {}
        dic = dict()
        dic["id"] = id
        dic["rsp_code"] = rsp_code
        dic["rsp_msg"] = rsp_msg
        dic["tran_idn_num"] = tran_idn_num
    return dic


# --- UPDATE : POST
@app.post('/hanlim/update')
async def update(reqItems: ReqUpdateItems):
    print('REQ >>>', reqItems)
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        # update obj set data = 'ABC' where id = 1
        cursor.execute("update tbl_name set rsp_code = '" + reqItems.rsp_code + "' where id = " + str(reqItems.id))
        cursor.execute("update tbl_name set rsp_msg = '" + reqItems.rsp_msg + "' where id = " + str(reqItems.id))
        cursor.execute("update tbl_name set tran_idn_num = '" + reqItems.tran_idn_num + "' where id = " + str(reqItems.id))
        cursor.execute("select * from tbl_name where id = " + str(reqItems.id))
        conn.commit()
        id, rsp_code, rsp_msg, tran_idn_num = cursor.fetchone()
        # dic = {}
        dic = dict()
        dic["id"] = id
        dic["rsp_code"] = rsp_code
        dic["rsp_msg"] = rsp_msg
        dic["tran_idn_num"] = tran_idn_num
    return dic


# --- SELECT ONE : GET
@app.get('/hanlim/selectone')
async def selectOne(id: int):
    print('REQ >>> id = ', id)
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.execute("select * from tbl_name where id = " + str(id))
        id, rsp_code, rsp_msg, tran_idn_num = cursor.fetchone()
        # dic = {}
        dic = dict()
        dic["id"] = id
        dic["rsp_code"] = rsp_code
        dic["rsp_msg"] = rsp_msg
        dic["tran_idn_num"] = tran_idn_num
    return dic


# --- SELECT ALL : GET
@app.get('/hanlim/selectall')
async def selectAll():
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()

        cursor.execute("select * from tbl_name where 1 = 1")
        lstRes = []
        for id, rsp_code, rsp_msg, tran_idn_num in cursor.fetchall():
            dic = {}
            dic["id"] = id
            dic["rsp_code"] = rsp_code
            dic["rsp_msg"] = rsp_msg
            dic["tran_idn_num"] = tran_idn_num
            lstRes.append(dic)
    #dic = json.loads(lstRes)
    # dic['rsp_code'] = reqItems.code
    return lstRes


# --- DELETE : GET
@app.get('/hanlim/delete')
async def delete(id: int):
    print('REQ >>> id =', id)
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        # DELETE FROM 테이블명 WHERE 조건
        cursor.execute("delete from tbl_name where id = " + str(id))
        conn.commit()
    return {'result':'SUCCESS!'}


# --- DELETE ALL : GET
@app.get('/hanlim/deleteall')
async def deleteall():
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        # DELETE FROM 테이블명
        cursor.execute("delete from tbl_name")
        conn.commit()
    return {'result':'SUCCESS!'}


# --- DROP TABLE : GET
@app.get('/hanlim/droptbl')
async def droptbl():
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        # DROP TABLE 테이블명
        cursor.execute("drop table tbl_name")
        conn.commit()
    return {'result':'SUCCESS!'}


# --- DROP DB : GET
@app.get('/hanlim/dropdb')
async def dropdb():
    os.remove('./' + db_filename)
    return {'result':'SUCCESS!'}
