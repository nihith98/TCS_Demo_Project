<<<<<<< HEAD
from flask import Flask,render_template,request,url_for,redirect
=======
from flask import Flask,render_template,request
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7
from flask_sqlalchemy import SQLAlchemy
from admin_login import admin_login
import sql_write
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:Google@98@localhost:3306/Tariff_Module"
db = SQLAlchemy(app)
results=db.session.execute("select * from plandetails")
resdb=[]
for row in results:
    resdb.append(row)
########## Homepage ###################
@app.route('/')
def frontpage():
    return render_template("Customer.html",resdb=resdb)
##### HomePage after login failure #########
@app.route('/<msg>')
def frontpage_unsuccessful(msg):
    if msg == 'IP':
        msg = 'Incorrect password or username'
    return render_template('Customer.html', msg=msg)
=======
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
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7

####### Login Validation #######
@app.route('/admin_login', methods=['POST'])
def login_validation():
<<<<<<< HEAD
    msg=""
=======
    msg = ""
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7
    username = request.form['usrnm']
    password = request.form['passwd']
    result = admin_login(username, password)
    if result == 1:
<<<<<<< HEAD
        return redirect(url_for('admin_page'))
    msg = "IP"
    return redirect(url_for('frontpage_unsuccessful', msg=msg))

############ Admin page #################
@app.route('/admin')
def admin_page():
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', result=record)

############ Admin page after one iteration #############
@app.route('/admin/<msg>')
def adminpage(msg):
    record = sql_write.display_plan()
    if msg == 'DS':
        msg = 'Plan disabled successfully'
    elif msg == 'AS':
        msg = 'Plan added successfully'
    elif msg == 'US':
        msg = 'Plan updated successfully'
    elif msg == 'ES':
        msg = 'Plan enabled successfully'
    else:
        msg = 'Plan deleted successfully'
    return render_template('loginSuccess_page.html', result=record, msg=msg)
=======
        record = sql_write.display_plan()
        return render_template('loginSuccess_page.html', result=record)
    msg = "Incorrect password or username"
    return render_template('Customer.html', msg=msg)
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7

####### Register Plan #######
@app.route('/admin_login/register', methods=['POST'])
def register_plan():
    add_name = request.form['name']
    add_tariff = request.form['tariff']
    add_validity = request.form['valid']
    add_rental = request.form['rental']
    add_type = request.form['type']
    sql_write.add_plan(add_name,add_tariff,add_validity,add_rental,add_type)
<<<<<<< HEAD
    msg = 'AS'
    return redirect(url_for('adminpage', msg=msg))
=======
    msg = 'Plan added Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7

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
<<<<<<< HEAD
    msg = 'US'
    return redirect(url_for('adminpage', msg=msg))
=======
    msg = 'Plan updated Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7

######## Disable Plan ##########
@app.route('/admin_login/disable', methods=['POST'])
def disable_plan():
    up_id = request.form['id']
    sql_write.disable_plan(up_id)
<<<<<<< HEAD
    msg = 'DS'
    return redirect(url_for('adminpage',msg=msg))
=======
    msg = 'Plan disabled Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7

######## Enable Plan ########
@app.route('/admin_login/enable', methods=['POST'])
def enable_plan():
    up_id = request.form['id']
    sql_write.enable_plan(up_id)
<<<<<<< HEAD
    msg = 'ES'
    return redirect(url_for('adminpage', msg=msg))
=======
    msg = 'Plan enabled Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7

####### Delete Plan #########
@app.route('/admin_login/delete', methods=['POST'])
def delete_plan():
    up_id = request.form['id']
    sql_write.delete_plan(up_id)
<<<<<<< HEAD
    msg = 'DP'
    return redirect(url_for('adminpage', msg=msg))
=======
    msg = 'Plan deleted Successfully'
    record = sql_write.display_plan()
    return render_template('loginSuccess_page.html', msg=msg, result=record)
>>>>>>> 966c7c4d0c5950c74a8e77c2bc8262bb47005ed7

app.run(debug=True)