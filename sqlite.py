import sqlite3


connection = sqlite3.connect('mydatabase.db')


curs = connection.cursor()


sql = " CREATE TABLE  employee (number INTEGER PRIMARY KEY, name VARCHAR(20),age INTEGER,gender CHAR(1),position VARCHAR(20) , joining DATE);"
curs.execute(sql)


emp1 = " INSERT INTO  employee VALUES (12,'Remesh',54,'M','Senior Software Engineer','20-02-2020');"
emp2 = " INSERT INTO  employee VALUES (1,'Sarita',20,'F','Junior Software Engineer','20-02-2020');"
emp3 = " INSERT INTO  employee VALUES (2,'Karthik',33,'m',' Team lead Validation','20-02-2020');"
curs.execute(emp1)
curs.execute(emp2)
curs.execute(emp3)


connection.commit()


connection.close()