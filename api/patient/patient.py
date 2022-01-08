from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector

mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)
mydb.autocommit = True

# mycursor = mydb.cursor()

patientBp = Blueprint('patientBp', __name__, template_folder='templates',static_folder='static')

mycursor = mydb.cursor()

@patientBp.route('/')
def patientIndex():
    '''
    This is the index page for the patient that view some statics about latest
    operations and patients that are
    waiting for a patient
    '''

    return render_template("patientIndex.html")

@patientBp.route('/operations')
def viewOperations():
    '''
    This is the page that allows the patient
    to view and to add a new operation to the database
    using there api
    '''
    mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("doctorViewOperations.html",data=data)
@patientBp.route('/add' ,methods=['POST'])
def addPatient():
    #TODO
    if request.method == 'POST':
        ssn = request.form['ssn']
        name = request.form['name']
        medicalHistory = request.form['medicalHistory']
        illness = request.form['illness']
        bdate = request.form['bdate']
        phone = request.form['phone']
        image = request.files['image']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        gender = request.form['gender']
        Relatives_phone_Number = request.form['Relatives_phone_Number']
        sql = "INSERT INTO `operationsDB`.`Patient` (`ssn`,`name`,`medicalHistory`,`illness`,`bdate`,`phone`,`image`,`username`,`password`,`email`,`address`,`gender`,`Relatives_phone_Number`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (ssn,name,medicalHistory,illness,bdate,phone,image.read(),username,password,email,address,gender,Relatives_phone_Number)
        mycursor.execute(sql,val)
        mydb.commit()

    return redirect(url_for('adminBp.viewPatient'))


@patientBp.route('/update' ,methods=['POST'])
def updatePatient():
    #TODO
    #     
    return("TestRoom")

@patientBp.route('/delete/<ssn>' ,methods=['GET'])
def deletePatient(ssn):
    sql = "DELETE FROM Patient WHERE ssn="+ssn
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewPatient'))
   

