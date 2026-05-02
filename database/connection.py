# import mysql.connector as SQLC

# # database configuration
# def databaseConfig():
#     db_config = SQLC.connect(
#         host='localhost',
#         user = 'root',
#         password='root',
#         database = 'ecommerce1'
#     )


import mysql.connector as SQLC
import os

def databaseConfig():
    # detect PythonAnywhere
    if "pythonanywhere" in os.getcwd():
        return SQLC.connect(
            host='shilpa1317.mysql.pythonanywhere-services.com',
            user='shilpa1317',
            password='YOUR_ACTUAL_DB_PASSWORD',   # ⚠️ replace this
            database='shilpa1317$ecommerce1'
        )
    else:
        return SQLC.connect(
            host='localhost',
            user='root',
            password='root',
            database='ecommerce1'
        )