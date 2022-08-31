# Creating an sqlite3 database.

import sqlite3
import os

db_filename = 'hanlim.db'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:   # (X) db가 없다면,
        print('(X) Need to create schema')
    else:           # (O) db가 있다면,
        print('(O) Database exists, assume schema does, too.')
