
from flask import Flask,render_template,request,redirect,session,flash,url_for
from functools import wraps
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='highflyer123'
app.config['MYSQL_DB']='whitecaps'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)
 
#DRLogin
@app.route('/') 
@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        cur.execute("select * from doctor where Email=%s and Password1=%s",(email,pwd))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['username']=data["FirstName"]
            flash('Login Successfully','success')
            return redirect('home')
        else:
            cur.execute("select * from familymembers where Email=%s and Password1=%s",(email,pwd))
            data=cur.fetchone()
            if data:
                session['logged_in']=True
                session['username']=data["FirstName"]
                flash('Login Successfully','success')
                return redirect('home')
            else:
                flash('Invalid Login. Try Again','danger')
    return render_template("login.html")
  
#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized, Please Login','danger')
			return redirect(url_for('login'))
	return wrap
  
#DocRegistration  
@app.route('/doc',methods=['POST','GET'])
def doc():
    status=False
    if request.method=='POST':
        Fname=request.form["Fname"]
        Lname=request.form["Lname"]
        email=request.form["email"]
        phone=request.form["phone"]
        Hname=request.form["HospitalName"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        cur.execute("insert into doctor(FirstName,LastName,Email,phone,HospitalName,Password1) values(%s,%s,%s,%s,%s,%s)",(Fname,Lname,email,phone,Hname,pwd))
        mysql.connection.commit()
        cur.close()
        flash('Registration Successfully. Login Here...','success')
        return redirect('login')
    return render_template("doc.html",status=status)
#PatientRegister
@app.route('/pat',methods=['POST','GET'])
def pat():
    status=False
    if request.method=='POST':
        Fname=request.form["Fname"]
        Lname=request.form["Lname"]
        email=request.form["email"]
        phone=request.form["phone"]
        Location=request.form["Location"]
        medicalc=request.form["medicalc"]
        age=request.form["age"]
        gender=request.form["choose-g"]
        bloodg=request.form["Choose-bg"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        i=1

        cur.execute("insert into patient(FirstName,LastName,email,phone,Location,medicalc,Age,Gender,BloodGroup,Password1,DocID,CTID,FamID) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Fname,Lname,email,phone,Location,medicalc,age,gender,bloodg,pwd,i,i,i))
        mysql.connection.commit()
        i+=1
        cur.close()
        flash('Registration Successfully. Login Here...','success')
        return redirect('login')
    return render_template("pat.html",status=status)
#FamilyMemberRegister
@app.route('/famMember',methods=['POST','GET'])
def famMember():
    status=False
    if request.method=='POST':
        Fname=request.form["Fname"]
        Lname=request.form["Lname"]
        email=request.form["email"]
        phone=request.form["phone"]
        RelName=request.form["family-rel"]
        LocName=request.form["Location"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        
        cur.execute("insert into familymembers(FirstName,LastName,Contact,Email,Relation,Location,Password1) values(%s,%s,%s,%s,%s,%s,%s)",(Fname,Lname,phone,email,RelName,LocName,pwd))
        mysql.connection.commit()
        cur.close()
        flash('Registration Successfully. Login Here...','success')
        return redirect('login')
    return render_template("famMember.html",status=status)

#Home page
@app.route("/home")
@is_logged_in
def home():
	return render_template('home.html')
    
#logout
@app.route("/logout")
def logout():
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('login'))
    
if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)