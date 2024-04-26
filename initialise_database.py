import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import DictCursor

database = psycopg2.connect(
    database="postgres",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432"
)
database.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

DB_NAME = "worldline"

with database.cursor() as cursor:
    cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    for db in cursor.fetchall():
        if DB_NAME in db:
            print(f"dropping {DB_NAME}...")
            cursor.execute(f"drop database {DB_NAME};")

with database.cursor() as cursor:
    cursor.execute(f"create database {DB_NAME};")
    print(f"initialised {DB_NAME} database")

with database.cursor() as cursor:
    cursor.execute(f"drop table if exists transactions;")
    cursor.execute("""create table transactions (
                   transactionId VARCHAR(36),
                   transactionTime TIMESTAMP(0),
                   payerId VARCHAR(255),
                   merchantId VARCHAR(36),
                   callbackUrl VARCHAR(255),
                   amount MONEY,
                   currency VARCHAR(4),
                   description VARCHAR(20),
                   merchantUrl VARCHAR(255),
                   merchantOrderId VARCHAR(64),
                   userAgent VARCHAR(255),
                   userIpAddress VARCHAR(48),
                   status VARCHAR(16),
                   merchantIdCode BIGINT,
                   bankId VARCHAR(16),
                   transactionType VARCHAR(32)
    );""")

with database.cursor(cursor_factory=DictCursor) as cursor:
    cursor.execute("""SELECT * FROM transactions;""")
    print(cursor.fetchall())