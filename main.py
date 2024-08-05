import sqlite3
import io
from sqlite3 import Error

def sql_connection():
    try:
        conn = sqlite3.connect('Originaldatabase.db')
        return conn
    except Error:
        print(Error)

def sql_table(conn):
    cursor_object = conn.cursor()
    cursor_object.execute("""
                            CREATE TABLE IF NOT EXISTS student(
                          roll_no INTEGER PRIMARY KEY,
                          first_name TEXT,
                          last_name TEXT,
                          class TEXT,
                          stream TEXT,
                          addres TEXT)""")
    conn.commit()
    conn.close()

conn = sql_connection()
sql_table(conn)
