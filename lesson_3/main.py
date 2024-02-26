# from os import *
#
# from datetime import *
#
# print(datetime.now())
from sqlite3 import connect


conn = connect("db.sqlite3")
cur = conn.cursor()
cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR (32) NOT NULL DEFAULT ('Username') CHECK ( length(first_name) >= 2 ),
            email VARCHAR (128) NOT NULL UNIQUE
    );
""")
conn.commit()
