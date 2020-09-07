import mysql.connector
from sql_write import *

#Connection with mySQL
mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='Nihith@98',database='Tariff_Module')
print("Printing the database object")
print(mydb) #Prints type and address of Database

mycursor = mydb.cursor()

#mycursor.execute('CREATE DATABASE Tariff_Module')
print("Showing all the databases:")
mycursor.execute('SHOW DATABASES')

for x in mycursor:
    print(x)


#mycursor.execute('CREATE TABLE plans (plan_id INT AUTO_INCREMENT PRIMARY KEY)')

print("Showing all the tables:")
mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)


#mycursor.execute('ALTER TABLE plans ADD name VARCHAR(30)')
#mycursor.execute("ALTER TABLE plans ADD type CHAR(1)")
#mycursor.execute('ALTER TABLE plans ADD tariff FLOAT(4)')
#mycursor.execute('ALTER TABLE plans ADD validity INT')
#mycursor.execute('ALTER TABLE plans ADD rental VARCHAR(100)')
mycursor.execute("SELECT * FROM plans")

print(type(mycursor.description[1]))
for x in mycursor.description:
    print(x[0])

#add_plan('voice3',0.6,20,'NA','V',1)
#mycursor.execute("ALTER TABLE plans ADD enable_flag INT")
#disable_plan(4)
enable_plan(4)
delete_plan(5)
display_plan()
