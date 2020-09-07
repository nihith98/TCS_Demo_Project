import mysql.connector
mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='Nihith@98',database='Tariff_Module')
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE users (admin_id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(30), password VARCHAR(30))")
mycursor.execute("INSERT INTO users (username, password) VALUES ('root',12345),('admin',12345)")
mydb.commit()