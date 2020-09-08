import mysql.connector

def add_plan(add_name,add_tariff,add_validity,add_rental,add_type,enable_flag=1):
    mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='Nihith@98',database='Tariff_Module')
    add_cursor = mydb.cursor()
    strcmd = "INSERT INTO plans (name, tariff, validity, rental,type,enable_flag) VALUES ('"+add_name+"',"+str(add_tariff)+','+str(add_validity)+",'"+add_rental+"','"+add_type+"',"+str(enable_flag)+")" 
    print(strcmd)
    add_cursor.execute(strcmd)
    mydb.commit()
    add_cursor.close()
    return None

def update_plan(up_id,up_name,up_tariff,up_validity,up_rental,up_type,enable_flag=1):
    mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='Nihith@98',database='Tariff_Module')
    update_cursor = mydb.cursor()
    strcmd = "UPDATE plans SET name='"+up_name+"',tariff="+str(up_tariff)+",validity="+str(up_validity)+",rental='"+up_rental+"',type='"+up_type+"',enable_flag="+str(enable_flag)+" WHERE plan_id="+str(up_id)
    print(strcmd)
    update_cursor.execute(strcmd)
    mydb.commit()
    update_cursor.close()
    return None

def disable_plan(up_id):
    mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='Nihith@98',database='Tariff_Module')
    disable_cursor = mydb.cursor()
    strcmd = "UPDATE plans SET enable_flag="+str(0)+" WHERE plan_id="+str(up_id)
    disable_cursor.execute(strcmd)
    mydb.commit()
    disable_cursor.close()
    return None

def enable_plan(up_id):
    mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='Nihith@98',database='Tariff_Module')
    enable_cursor = mydb.cursor()
    strcmd = "UPDATE plans SET enable_flag="+str(1)+" WHERE plan_id="+str(up_id)
    enable_cursor.execute(strcmd)
    mydb.commit()
    enable_cursor.close()
    return None

def delete_plan(up_id):
    mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='Nihith@98',database='Tariff_Module')
    del_cursor = mydb.cursor()
    strcmd = "DELETE FROM plans WHERE plan_id="+str(up_id)
    del_cursor.execute(strcmd)
    mydb.commit()
    del_cursor.close()
    return None
    
def display_plan():
    connection = mysql.connector.connect(host='127.0.0.1',database='Tariff_Module',user='root',password='Nihith@98')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select * from plan;")
        record = cursor.fetchall()
        if record !=None:
            print("{:<15}{:<22}{:<10}{:<10}{:<10}{:<10}{:<20}".format("Plan_ID","Name","Tarrif","Validity","Rental","Type","Enable_Flag"))
            for i in range(len(record)):
                print("{:<15}{:<22}{:<10}{:<10}{:<10}{:<10}{:<20}".format(record[i][0],record[i][1],record[i][2],record[i][3],record[i][4],record[i][5],record[i][6]))
    cursor.close()
    connection.close()
    return None
