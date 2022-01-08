from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector
from base64 import b64encode

# mycursor = mydb.cursor()
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)
doctorBp = Blueprint('doctorBp', __name__, template_folder='templates',static_folder='static')
mycursor = mydb.cursor()
@doctorBp.route('/')
def doctorIndex():
    '''
    This is the index page for the doctor that view some statics about latest
    operations and patients that are
    waiting for a doctor
    '''

    return render_template("doctorIndex.html")

@doctorBp.route('/operations')
def viewOperations():
    '''
    This is the page that allows the doctor
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

@doctorBp.route('/operations/add')
def addOperations():
    '''
    This is the page that allows the doctor
    to view and to add a new operation to the database
    using there api
    '''
    return render_template("doctorAddOperation.html")

@doctorBp.route('/patients')
def viewPatients():
    '''
    This is the page that allows the doctor
    to view patients in a table
    '''

    mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("doctorViewPatients.html",data=data)

@doctorBp.route('/patients/<patient_id>')
def viewPatient(patient_id):
    '''
    This is the page that allows the admin to view one patient page
    '''
    mycursor.execute("SELECT name,medicalHistory,email,image,phone,gender,bdate,address,ssn,illness,Relatives_phone_Number FROM operationsDB.Patient WHERE ssn="+ patient_id)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4],r[5],r[6],r[7],r[8],r[9],r[10]) for r in myresult]

    return render_template("doctorViewPatient.html",data=myresult)

@doctorBp.route('/nurses')
def viewNurses():
    '''
    This is the page that allows the doctor
    to view nurses in a table
    '''

    mycursor.execute("SELECT name,birthdate,address,currentOperation,superSsn,salary,biography,phone,gender FROM operationsDB.Nurse")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("doctorViewNurses.html",data=data)

@doctorBp.route('/rooms')
def viewRooms():
    '''
    This is the page that allows the doctor
    to view rooms in a table
    '''

    mycursor.execute("SELECT * FROM operationsDB.`Operation Room`;")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("doctorViewRooms.html",data=data)

@doctorBp.route('/add' ,methods=['POST'])
def addDoctor():
    '''
    This is add POST request for the doctor
    that add a new doctor to the database
    '''
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        ssn = request.form['ssn']
        biography = request.form['biography']
        gender = request.form['gender']
        birthdate = request.form['birthdate']
        phone = request.form['phone']
        address = request.form['address']
        image = request.files['image']
        sql = "INSERT INTO `operationsDB`.`Doctor` (`name`, `username`, `password`, `biography`, `phoneNumber`, `email`, `gender`, `birthdate`, `ssn`, `address`,`image`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (name,username,password,biography,phone,email,gender,birthdate,ssn,address,image.read())
        mycursor.execute(sql,val)
        mydb.commit()
        # print(name,username,password,biography,phone,email,gender,birthdate,ssn,address,image.read())

    return render_template("adminAddDoctor.html")

@doctorBp.route('/update' ,methods=['PUT'])
def updateDoctor():
    '''
    This is update PUT request for the doctor
    that update a doctor in the database
    '''    
    return("Test")

@doctorBp.route('/delete/<ssn>' ,methods=['GET'])
def deleteDoctor(ssn):
    sql = "DELETE FROM Doctor WHERE ssn="+ssn
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewDoctors'))
