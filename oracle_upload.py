import getpass
import oracledb
from dotenv import load_dotenv
import os
import requests

if __name__ == "__main__":
    connection=oracledb.connect(
        config_dir="C:/workspace/notam_llm/wallet",
        user=os.getenv("user"),
        password=os.getenv("pw"),
        dsn="sljmdb_high",
        wallet_location="C:/workspace/MPA/wallet",
        wallet_password=os.getenv("wallet_pw"),
        )

    print("Successfully connected to Oracle Database")

    statement = "INSERT into NOTAM (NOTAM_ID, FROM_TIME,TO_TIME,LOWER,UPPER,EVENT,GEO_DOC) VALUES (:1,:2,:3,:4,:5,:6,:7)"

    print(statement)

'''
    with connection.cursor() as cursor:
        cursor.executemany(statement, data)
        print(cursor.rowcount, "Rows Inserted")

    connection.commit()
'''