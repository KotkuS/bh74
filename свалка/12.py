from enum import IntEnum


class Status(IntEnum):
    TO_DO = 0
    IN_PROGRESS = 1

from psycopg2 import connect
from psycopg2._psycopg import cursor
from datetime import datetime

with connect(dsn="postgres://user8:O8Je0iSal@217.76.60.77:6666/") as conn:
    with conn.cursor() as cur:  # type: cursor
        cur.execute("""
            CREATE TABLE IF NOT EXISTS projects(
                id INTEGER PRIMARY KEY,
                name VARCHAR(16) NOT NULL UNIQUE
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                project_id INTEGER NOT NULL, 
                FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                title VARCHAR NOT NULL CHECK (length(title) >= 2),
                description TEXT,
                start_date TIMESTAMP NOT NULL,
                end_date TIMESTAMP NOT NULL,
                author_id INTEGER NOT NULL, 
                FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                executor_id INTEGER NOT NULL, 
                FOREIGN KEY (executor_id) REFERENCES executor(id) ON DELETE RESTRICT ON UPDATE CASCADE
            ); 
        """)
conn.commit()
