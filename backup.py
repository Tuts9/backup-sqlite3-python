import sqlite3
import io
import os
from sqlite3 import Error
import datetime

data = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

os.mkdir(f'backup_{data}')

def sql_connection():
    try:
        conn = sqlite3.connect('Originaldatabase.db')
        return conn
    except Error:
        print(Error)

conn = sql_connection()

with io.open(f'./backup_{data}/backupdatabase_dump.sql', 'w') as p:
    for line in conn.iterdump():
        p.write('%s\n' % line)

print('Backup performed succesfully!')
print('Data Saved as backupdatabase_dump.sql')

conn.close()