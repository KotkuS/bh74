from enum import IntEnum
from sqlalchemy import Enum, Column
from datetime import date


class Status(IntEnum):
    TO_DO = 0
    IN_PROGRESS = 1
    DONE = 2


Column(Enum(Status))


from psycopg2 import connect
from psycopg2._psycopg import cursor


with connect(dsn="postgres://user8:O8Je0iSal@217.76.60.77:6666/user8") as conn:
    with conn.cursor() as cur:  # type: cursor
        cur.execute("""
            CREATE TABLE IF NOT EXISTS projects(
                id INTEGER PRIMARY KEY,
                name VARCHAR(16) NOT NULL UNIQUE check (length(name) >= 1)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS USERS_(
                id INTEGER PRIMARY KEY,
                name VARCHAR(16) NOT NULL check (length(name) >= 1)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                project_id INTEGER NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects(id),
                title VARCHAR NOT NULL CHECK (length(title) >= 2),
                description TEXT,
                start_date TIMESTAMP NOT NULL,
                end_date TIMESTAMP NOT NULL,
                author_id INTEGER NOT NULL,
                FOREIGN KEY (author_id) REFERENCES users(id),
                executor_id INTEGER NOT NULL,
                FOREIGN KEY (executor_id) REFERENCES users(id),
                status Enum NOT NULL
            );
        """)
conn.commit()
