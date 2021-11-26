import sqlite3
from training import rec

conn = sqlite3.connect('lab1.db')
cur = conn.cursor()
print("Connected to SQLite")


def create_table():
    query = cur.execute('''CREATE TABLE tab(
        title TEXT,
        subscribe TEXT,
        href TEXT,
        PRIMARY KEY(href))''')
    print("Table was created")
    conn.commit()

    return query


def insert_data(data):
    ins_data = cur.executemany("INSERT INTO tab VALUES(?,?,?)", (data))
    print("Data were inserted!")
    conn.commit()

    return ins_data


def fetch_data():
    cur.execute("SELECT * FROM hrefs")
    rows = cur.fetchall()
    return rows


def drop_table():
    drop = cur.execute("DROP TABLE IF EXISTS tab")
    print("Table was dropped")
    return drop


insert_data(rec)
