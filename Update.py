import sqlite3

connection = sqlite.connect("./my-database.db")

cursor = connection.cursor()

sql = """
    UPDATE product SET productName="vuejs cours edited" WHERE productId = 3
"""

cursor.execute(sql)
connetction.commit()
connetction.close()