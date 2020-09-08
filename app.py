from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:Sneha123@localhost:3306/Plandetails"
db = SQLAlchemy(app)
results=db.session.execute("select * from planandtariff")
resdb=[]
for row in results:
    resdb.append(row)

@app.route('/', methods=['GET','POST'])
def frontpage():
    return render_template("Customer.html",resdb=resdb)

app.run()