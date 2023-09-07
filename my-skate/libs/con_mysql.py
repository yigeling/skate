import pymysql
from config.settings import DB_SCHEM, DB_PASS, DB_USER, DB_PORT, DB_HOST

def connect_mysql():
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_SCHEM
    )

    return conn