import sqlite3

connection = sqlite.connect("./my-database.db")

cursor = connection.cursor()

sql = """
    DELETE Product SET productName="vuejs course edited" WHERE productId = 3
"""

cursor.execute(sql)
connetction.commit()
connetction.close()

#ORM =>  object relational mapping