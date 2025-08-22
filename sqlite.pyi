import sqlite3

connection = sqlite.connect("./my-database.db")

cursor = connection.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS user (
    productId INTIGER ,
    productName VARCHAR (60),
    price INTEGER (60),
    description VARCHAR (60) 
    );
"""


# sql = """
#     CREATE TABLE IF NOT EXISTS user (
#     userId INTIGER ,
#     name VARCHAR (60),
#     family VARCHAR (60),
#     email VARCHAR (60)
#     );
# """

cursor.execute(sql)
connetction.commit()

connetction.close()
