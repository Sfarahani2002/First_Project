import sqlite3

connection = sqlite.connect("./my-database.db")

cursor = connection.cursor()
sql = """
    INSERT INTO product VALUES (1, 'python course', 2000, ' this is python course');
"""


sql = """
    INSERT INTO product VALUES (2, 'kotlin course', 3000, ' this is kotlin course');
    INSERT INTO product VALUES (3, 'vue course', 4000, ' this is vue course');
"""
# cursor.execute(sql)

cursor.executescript(sql)  # => chand item hamzaman
connetction.commit()
connetction.close()
