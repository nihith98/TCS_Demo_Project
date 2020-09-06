import mysql.connector

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
