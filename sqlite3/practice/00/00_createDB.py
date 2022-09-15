import sqlite3
import os

db_filename = 'test.db'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:   # db가 없다면,
        print('(X) Database has been created.')
    else:           # db가 있다면,
        print('(O) Database exists.')