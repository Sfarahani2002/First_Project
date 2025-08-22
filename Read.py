import sqlite3

connection = sqlite.connect("./my-database.db")

cursor = connection.cursor()

# sql = """
    # SELECT * FROM product WHERE productId = 1
# """

sql = """
    SELECT * FROM product WHERE DESCRIPTION like "%python% = 1
"""

cursor.execute(sql)

for product in cursor:
    print(product)

connetction.commit()
connetction.close()