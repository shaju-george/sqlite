Here, we are going to connect SQLite with Python. Python has a native library for SQLite.

1) To use SQLite, we must import sqlite3.
2) Then create a connection using connect() method and pass the name of the database you want to access if there is a file with that name, it will open that file. Otherwise, Python will create a file with the given name.
3) After this, a cursor object is called to be capable to send commands to the SQL. Cursor is a control structure used to traverse and fetch the records of the database. Cursor has a major role in working with Python. All the commands will be executed using cursor object only.
4) To create a table in the database, create an object and write the SQL command in it with being commented. 
5) And executing the command is very easy. Call the cursor method execute and pass the name of the sql command as a parameter in it. Save a number of commands as the sql_comm and execute them. After you perform all your activities, save the changes in the file by committing those changes and then lose the connection.


Fetching the data from record is same as the inserting them. The execute method uses the SQL command of getting all the data from the table using “Select * from table_name” and all the table data can be fetched in an object in the form of list of lists.