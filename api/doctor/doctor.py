from flask import Flask,Blueprint, redirect, url_for, request,render_template, session
import mysql.connector
from base64 import b64encode
import os
import datetime
import os.path
from flask_cors import CORS, cross_origin

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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

CLIENT_SECRET_FILE = "client_secret_240695600096-ndnm8sahb9f9p117913u6ugkhak9rlq1.apps.googleusercontent.com.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ['https://www.googleapis.com/auth/calendar']

@doctorBp.route('/')
def doctorIndex():
    '''
    This is the index page for the doctor that view some statics about latest
    operations and patients that are
    waiting for a doctor
    '''
    if not session.get("id"):
        return redirect(url_for('homeBp.login'))
    mycursor.execute("SELECT name,email,username FROM Doctor WHERE ssn = "+str(session.get("id")))
    result = mycursor.fetchall()[0]
    name = result[0]
    email = result[1]
    username = result[2]
    session['name'] = name
    session['email'] = email
    session['username'] = username
    session['accountType'] = "doctor"
    creds = None

    if session.get("token"):
        creds = Credentials(token=session.get("token"),
            refresh_token=session.get("refresh_token"),
            token_uri="https://oauth2.googleapis.com/token", 
            client_id=session.get("client_id"),
            client_secret=session.get("client_secret"),
            scopes=SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret_240695600096-ndnm8sahb9f9p117913u6ugkhak9rlq1.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server()
            session['token'] = creds.token
            session['refresh_token'] = creds.refresh_token
            session['client_id'] = creds.client_id
            session['client_secret'] = creds.client_secret
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
    except HttpError as error:
        print('An error occurred: %s' % error)

    return render_template("doctorIndex.html")

@doctorBp.route('/operations')
def viewOperations():
    '''
    This is the page that allows the doctor
    to view and to add a new operation to the database
    using there api
    '''
    search = request.args.get('search')
    date = request.args.get('date')
    type = request.args.get('type')
    if type == 'name':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time', Room_Location AS 'Room Location' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn JOIN `Operation Room` ON roomId = Operation_Room_ID WHERE Operation.operationName LIKE '%"+search+"%'")
    elif type == 'patient':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time', Room_Location AS 'Room Location' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn JOIN `Operation Room` ON roomId = Operation_Room_ID WHERE Patient.name LIKE '%"+search+"%'")
    elif type == 'id':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time', Room_Location AS 'Room Location' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn JOIN `Operation Room` ON roomId = Operation_Room_ID WHERE Operation.id LIKE '%"+search+"%'")
    elif type == 'doctor':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time', Room_Location AS 'Room Location' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn JOIN `Operation Room` ON roomId = Operation_Room_ID WHERE Doctor.name LIKE '%"+search+"%'")
    elif type == 'date':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time', Room_Location AS 'Room Location' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn JOIN `Operation Room` ON roomId = Operation_Room_ID WHERE date LIKE '%"+date+"%'")
    else :
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time', Room_Location AS 'Room Location' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn JOIN `Operation Room` ON roomId = Operation_Room_ID")
    
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

    search = request.args.get('search')
    type = request.args.get('type')
    if type == 'name':
        mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient WHERE Patient.name  LIKE '%"+search+"%'")
    elif type == 'ssn':
        mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient WHERE Patient.ssn LIKE '%"+search+"%'")
    elif type == 'age':
        mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient WHERE 2022-YEAR(bdate) LIKE '%"+search+"%'")
    else:
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
    search = request.args.get('search')
    if search == None:
        search = ""
    #mycursor.execute("SELECT name,biography,email,image,phone,gender,birthdate,address,ssn FROM operationsDB.Nurse WHERE ssn="+ Nurse_id)
    mycursor.execute("SELECT name,biography,email,image,ssn FROM operationsDB.Nurse WHERE name LIKE '%"+search+"%' ORDER BY name ")

    #mycursor.execute("SELECT name,biography,email,image,ssn FROM operationsDB.Nurse")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4]) for r in myresult]
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("doctorViewNurses.html",data=data)

@doctorBp.route('/nurses/<Nurse_id>')
def viewNurse(Nurse_id):
    '''
    This is the page that allows the admin to view one Nurse page
    '''

    mycursor.execute("SELECT name,biography,email,image,phone,gender,birthdate,address,ssn FROM operationsDB.Nurse WHERE ssn="+ Nurse_id)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4],r[5],r[6],r[7],r[8]) for r in myresult]

    return render_template("doctorViewNurse.html",data=myresult)

@doctorBp.route('/rooms')
def viewRooms():
    '''
    This is the page that allows the doctor
    to view rooms in a table
    '''

    search = request.args.get('search')
    type = request.args.get('type')
    if type == 'location':
        mycursor.execute("SELECT * FROM operationsDB.`Operation Room` WHERE Room_Location LIKE '%"+search+"%'")
    elif type == 'id':
        mycursor.execute("SELECT * FROM operationsDB.`Operation Room` WHERE Operation_Room_ID LIKE '%"+search+"%'")
    else :
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

@doctorBp.route('/patients/<patient_id>/addfile' ,methods=['POST'])
def addFile(patient_id):
    '''
    This is add POST request for the doctor
    that add a new doctor to the database
    '''

    if request.method == 'POST':
        file = request.files['image']
        sql = "INSERT INTO `operationsDB`.`File` (`name`, `extension`, `data`, `doctorId`, `patientId`) VALUES (%s,%s,%s,%s,%s);"
        val = (file.filename ,file.filename.rsplit('.', 1)[1].lower(),file.read(),str(session.get("id")),patient_id)
        mycursor.execute(sql,val)
        mydb.commit()
        return redirect(url_for('doctorBp.viewPatients'))

        # print(name,username,password,biography,phone,email,gender,birthdate,ssn,address,image.read())

    return render_template("adminAddDoctor.html")

@doctorBp.route('/update/<ssn>' ,methods=['POST', 'GET'])
def updateDoctor(ssn):

    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        ssn = request.form['ssn']
        biography = request.form['biography']
        gender = request.form['gender']
        birthdate = request.form['birthdate']
        phoneNumber = request.form['phone']
        address = request.form['address']
        image = request.files['image']

        if image.filename == '':
            sql = "UPDATE `operationsDB`.`Doctor` SET ssn=%s,name=%s,birthdate=%s,address=%s,biography=%s,phoneNumber=%s,gender=%s,username=%s,email=%s,password=%s WHERE ssn="+ssn
            val = (ssn,name,birthdate,address,biography,phoneNumber,gender,username,email,password)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            sql = "UPDATE `operationsDB`.`Doctor` SET ssn=%s,name=%s,birthdate=%s,address=%s,biography=%s,phoneNumber=%s,gender=%s,username=%s,email=%s,password=%s,image=%s WHERE ssn="+ssn
            val = (ssn,name,birthdate,address,biography,phoneNumber,gender,username,email,password,image.read())
            mycursor.execute(sql,val)
            mydb.commit()

        

    return redirect(url_for('adminBp.viewDoctors'))

@doctorBp.route('/delete/<ssn>' ,methods=['GET'])
def deleteDoctor(ssn):
    sql = "DELETE FROM Doctor WHERE ssn="+ssn
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewDoctors'))
