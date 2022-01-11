from flask import Flask,Blueprint, redirect, sessions, url_for, request,render_template,flash,session
import pandas as pd
from home.forms import LoginForm,ContactForm
import mysql.connector
# mycursor = mydb.cursor()
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)
mycursor = mydb.cursor()

homeBp = Blueprint('homeBp', __name__, template_folder='templates',static_folder='static')

@homeBp.route('/', methods=["GET", "POST"])
def login():
    form=LoginForm()
    if request.method == 'POST':
        un = request.form.get("username")
        pw = request.form.get("password")
        
        mycursor.execute("SELECT username, password, id FROM operationsDB.Admin")
        myresult = mycursor.fetchall()
        for adminCredentials in myresult:
            if un == adminCredentials[0] and pw == adminCredentials[1] :
                session["id"] = adminCredentials[2] 
                session["accountType"] = "admin"
                session.modified = True
                return redirect(url_for('adminBp.index'))
        
        mycursor.execute("SELECT username, password, ssn FROM operationsDB.Doctor")
        myresult = mycursor.fetchall()
        for doctorCredentials in myresult:
            if un == doctorCredentials[0] and pw == doctorCredentials[1] :
                session["id"] = doctorCredentials[2] 
                session["accountType"] = "doctor"
                session.modified = True
                return redirect(url_for('doctorBp.doctorIndex'))
        
        mycursor.execute("SELECT username, password, ssn FROM operationsDB.Nurse")
        myresult = mycursor.fetchall()
        for nurseCredentials in myresult:
            if un == nurseCredentials[0] and pw == nurseCredentials[1] :
                session["id"] = nurseCredentials[2] 
                session["accountType"] = "nurse"
                session.modified = True
                return redirect(url_for('nurseBp.nurseIndex'))
        
        mycursor.execute("SELECT username, password, ssn FROM operationsDB.Patient")
        myresult = mycursor.fetchall()
        for patientCredentials in myresult:
            if un == patientCredentials[0] and pw == patientCredentials[1] :
                session["id"] = patientCredentials[2] 
                session["accountType"] = "patient"
                session.modified = True
                return redirect(url_for('patientBp.patientIndex'))
    else:
        return render_template('home.html', form=form)

@homeBp.route('/Contactus',methods=["GET", "POST"])
def contactus():
    form=ContactForm()
    if request.method == 'POST':
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv', mode='a',index=False ,header=None)
        flash('Form submitted.')
        return render_template('Contactus.html',form=form)
    else:
        return render_template('Contactus.html',form=form)

    