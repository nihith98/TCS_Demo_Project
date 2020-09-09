from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from admin_login import admin_login
import sql_write
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:Nihith@98@localhost:3306/Tariff_Module"
db = SQLAlchemy(app)
results=db.session.execute("SELECT * FROM plans WHERE enable_flag=1")
resdb=[]
for row in results:
    resdb.append(row)
##### HomePage #########
@app.route('/', methods=['GET','POST'])
def frontpage():
    return render_template("Customer.html",resdb=resdb)

####### Login Validation #######
@app.route('/admin_login', methods=['POST'])
def login_validation():
    msg = ""
    username = request.form['usrnm']
    password = request.form['passwd']
    result = admin_login(username, password)
    if result == 1:
        record = sql_write.display_plan()
        return render_template('loginSuccess_page.html', result=record)
    msg = "Incorrect password or username"
    return render_template('Customer.html', msg=msg)

####### Register Plan #######
@app.route('/admin_login/register', methods=['POST'])
def register_plan():
    add_name = request.form['name']
    add_tariff = request.form['tariff']
    add_validity = request.form['valid']
    add_rental = request.form['rental']
    add_type = request.form['type']
    sql_write.add_plan(add_name,add_tariff,add_validity,add_rental,add_type)
    msg = 'Plan added Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)

######## Update Plan ########
@app.route('/admin_login/update', methods=['POST'])
def update_plan():
    up_id = request.form['id']
    up_name = request.form['name']
    up_tariff = request.form['tariff']
    up_validity = request.form['valid']
    up_rental = request.form['rental']
    up_type = request.form['type']
    sql_write.update_plan(up_id,up_name,up_tariff,up_validity,up_rental,up_type)
    msg = 'Plan updated Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)

######## Disable Plan ##########
@app.route('/admin_login/disable', methods=['POST'])
def disable_plan():
    up_id = request.form['id']
    sql_write.disable_plan(up_id)
    msg = 'Plan disabled Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)

######## Enable Plan ########
@app.route('/admin_login/enable', methods=['POST'])
def enable_plan():
    up_id = request.form['id']
    sql_write.enable_plan(up_id)
    msg = 'Plan enabled Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)

####### Delete Plan #########
@app.route('/admin_login/delete', methods=['POST'])
def delete_plan():
    up_id = request.form['id']
    sql_write.delete_plan(up_id)
    msg = 'Plan deleted Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)

app.run(debug=True)