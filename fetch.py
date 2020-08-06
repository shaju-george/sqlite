
import sqlite3

connection = sqlite3.connect("mydatabase.db")

curs = connection.cursor()

sql_command = ''' SELECT * FROM employee; '''

curs.execute(sql_command)

data = curs.fetchall()

print(data)

curs.close()