import mysql.connector

def admin_login(username,passwd):
    flag = 0
    mydb = mysql.connector.connect(user='root',password='Nihith@98',database='Tariff_Module',host='127.0.0.1')
    login_cursor = mydb.cursor()
    login_cursor.execute("SELECT * FROM users")
    for x in login_cursor:
        print(x)
        if x[1] == username:
            if x[2] == passwd:
                flag = 1
    return flag