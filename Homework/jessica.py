import mysql.connector

connection = mysql.connector.connect(host = 'localhost',
                                     port = '3306',
                                     user = 'root',
                                     password = 'Antony990715',
                                     database = 'sql_tutorial')

cursor1 = connection.cursor()

# cursor1.execute("SHOW DATABASES;")
# records = cursor1.fetchall()
# cursor1.execute("USE `sql_tutorial`;")

cursor1.execute("SELECT * FROM `employee`;")
records = cursor1.fetchall()

cursor1.close()
connection.commit()
connection.close()