from psycopg2 import connect
from psycopg2._psycopg import cursor
from psycopg2.extras import NamedTupleCursor
from datetime import datetime

with connect(dsn="postgres://user8:O8Je0iSal@217.76.60.77:6666/user8") as conn:
    with conn.cursor() as cur:  # type: cursor
        cur.execute("""
            CREATE TABLE IF NOT EXISTS department(
                id INTEGER PRIMARY KEY,
                name VARCHAR(32) NOT NULL CHECK (length(name) >= 2)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sub_department(
                id INTEGER PRIMARY KEY,
                name VARCHAR(32) NOT NULL CHECK (length(name) >= 2)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS chats(
                id INTEGER PRIMARY KEY,
                name VARCHAR(32) NOT NULL CHECK (length(name) >= 2)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                department_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES department(id),
                sub_department_id INTEGER,
                FOREIGN KEY (sub_department_id) REFERENCES sub_department(id)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS chats_relations(
                id INTEGER PRIMARY KEY,
                chat_id INTEGER NOT NULL,
                FOREIGN KEY (chat_id) REFERENCES chats(id),
                department_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES department(id),
                sub_department_id INTEGER,
                FOREIGN KEY (sub_department_id) REFERENCES sub_department(id)
            );
        """)
conn.commit()
with conn.cursor() as cur:  # type: cursor
    cur.execute("""
        SELECT chats.name FROM chats_relations
        JOIN chats ON chats.id = chats_relations.chat_id
        WHERE (
            chats_relations.department_id is null or 
            chats_relations.department_id = ( select users.department_id from users where users.id = %(user_id)s)
        ) and (
            chats_relations.sub_department_id is null or 
            chats_relations.sub_department_id = ( select users.sub_department_id from users where users.id = %(user_id)s)
        );
    """, {"user_id": 1})
    print(cur.fetchall())
