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

def databaseConfig():
    db_config = SQLC.connect(
        host='shilpa1317.mysql.pythonanywhere-services.com',
        user='shilpa1317',
        password='YOUR_DB_PASSWORD',
        database='shilpa1317$ecommerce1'
    )
    return db_config