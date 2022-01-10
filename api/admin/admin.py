from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector
from base64 import b64encode

adminBp = Blueprint('adminBp', __name__, template_folder='templates',static_folder='static')
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB",autocommit=True
)
mydb.autocommit = True
mycursor = mydb.cursor()

@adminBp.route('/')
def index():
    #Patients Gender
    mycursor.execute("SELECT COUNT(ssn) FROM operationsDB.Patient WHERE gender='female';")
    femalesNum = mycursor.fetchall();
    mycursor.execute("SELECT COUNT(ssn) FROM operationsDB.Patient WHERE gender='male';")
    malesNum = mycursor.fetchall();
    
    #Nurses Gender
    mycursor.execute("SELECT COUNT(ssn) FROM operationsDB.Nurse WHERE gender='female';")
    femalesNurses = mycursor.fetchall();
    mycursor.execute("SELECT COUNT(ssn) FROM operationsDB.Nurse WHERE gender='male';")
    malesNurses = mycursor.fetchall();

    values = [];
    #Operations Months
    for i in range(12):
        mycursor.execute("SELECT Count(id) FROM operationsDB.Operation WHERE MONTH(date) ="+ str(i+1) +";")
        values.append(mycursor.fetchall()[0][0])

    dataPatient = {'Task' : 'Hours per Day', 'Male' : malesNum[0][0], 'Female' : femalesNum[0][0]}
    dataNurses = {'Task' : 'Hours per Day', 'Male' : malesNurses[0][0], 'Female' : femalesNurses[0][0]}
    dataOperations = {'Month' : 'Number', 
    'January'   : values[0], 
    'February'  : values[1],
    'March'     : values[2], 
    'April'     : values[3],
    'May'       : values[4], 
    'June'      : values[5],
    'July'      : values[6], 
    'August'    : values[7],
    'September' : values[8], 
    'October'   : values[9],
    'November'  : values[10], 
    'December'  : values[11],
    }

    return render_template('adminDashboard.html',patients=dataPatient,nurses=dataNurses,operations=dataOperations)

#Operations
@adminBp.route('/operations')
def viewOperations():
    '''
    This is the page that allows the admin
    to view and to add a new operation to the database
    using there api
    '''
    search = request.args.get('search')
    date = request.args.get('date')
    type = request.args.get('type')
    if type == 'name':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn WHERE Operation.operationName LIKE '%"+search+"%'")
    elif type == 'patient':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn WHERE Patient.name LIKE '%"+search+"%'")
    elif type == 'id':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn WHERE Operation.id LIKE '%"+search+"%'")
    elif type == 'doctor':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn WHERE Doctor.name LIKE '%"+search+"%'")
    elif type == 'date':
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn WHERE date LIKE '%"+date+"%'")
    else :
        mycursor.execute("SELECT id as ID ,operationName as 'Operation Name', Patient.name as 'Patient Name', Doctor.name as 'Doctor Name', date as Date,startTime as 'Start Time', endTime as 'End Time' FROM Operation JOIN Patient ON Operation.patientId = Patient.ssn JOIN Doctor on Operation.doctorID = Doctor.ssn")
    
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }

    return render_template("adminViewOperations.html",data=data)

@adminBp.route('/operations/add')
def addOperations():
    '''
    This is the page that allows the admin
    to view and to add a new operation to the database
    using there api
    '''
    return render_template("adminAddOperation.html")

#Equipments
@adminBp.route('/equipment')
def viewEquipment():
    '''
    This is the page that allows the admin
    to view equipment in a table
    '''
    search = request.args.get('search')
    type = request.args.get('type')
    if type == 'name':
        mycursor.execute("SELECT * FROM operationsDB.Equipment WHERE Equipment.Equipment_Name LIKE '%"+search+"%'")
    elif type == 'id':
        mycursor.execute("SELECT * FROM operationsDB.Equipment WHERE Equipment.Equipment_ID LIKE '%"+search+"%'")
    elif type == 'room':
        mycursor.execute("SELECT * FROM operationsDB.Equipment WHERE Equipment.Eq_room LIKE '%"+search+"%'")
    
    else :
        mycursor.execute("SELECT * FROM operationsDB.Equipment")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewEquipment.html",data=data)

@adminBp.route('/equipment/add')
def addEquipment():
    '''
    This is the page that allows the admin
    to view and to add a new equipment to the database
    using there api
    '''

    return render_template("adminAddEquipment.html")

#Patients

@adminBp.route('/patients')
def viewPatient():
    '''
    This is the page that allows the admin
    to view patient in a table
    '''
    search = request.args.get('search')
    type = request.args.get('type')
    if type == 'name':
        mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient WHERE Patient.name  LIKE '%"+search+"%'")
    elif type == 'ssn':
        mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient WHERE Patient.ssn LIKE '%"+search+"%'")
    elif type == 'age':
        mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient WHERE Patient.bdate LIKE '%"+search+"%'")
    
    else :
        mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient")
    
    #mycursor.execute("SELECT ssn as SSN,name as Name ,phone as 'Phone Number',illness as Illness,2022-YEAR(bdate) as AGE FROM operationsDB.Patient WHERE name LIKE '%"+search+"%' ORDER BY name  ")
   #mycursor.execute("SELECT ssn,name  ,phone ,illness,2022-YEAR(bdate) operationsDB.Patient WHERE name LIKE '%"+search+"%' ORDER BY name  ")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    
    myresult = mycursor.fetchall()
   # myresult = [(r[0],r[1],r[2],r[3],r[4]) for r in myresult]
    
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewPatients.html",data=data)

@adminBp.route('/patients/add')
def addPatients():
    '''
    This is the page that allows the admin to view nurses in a table
    '''
    return render_template("adminAddPatient.html")

@adminBp.route('/patients/<patient_id>')
def viewpatient(patient_id):
    '''
    This is the page that allows the admin to view one patient page
    '''

    mycursor.execute("SELECT name,medicalHistory,email,image,phone,gender,bdate,address,ssn,illness,Relatives_phone_Number FROM operationsDB.Patient WHERE ssn="+ patient_id)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4],r[5],r[6],r[7],r[8],r[9],r[10]) for r in myresult]

    return render_template("adminViewPatient.html",data=myresult)

#Nurses
@adminBp.route('/nurses')
def viewNurses():
    '''
    This is the page that allows the admin to view nurses in a table
    '''
    search = request.args.get('search')
    if search == None:
        search = ""
    #mycursor.execute("SELECT name,biography,email,image,phone,gender,birthdate,address,ssn FROM operationsDB.Nurse WHERE ssn="+ Nurse_id)
    mycursor.execute("SELECT name,biography,email,image,ssn FROM operationsDB.Nurse WHERE name LIKE '%"+search+"%' ORDER BY name ")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4]) for r in myresult]

    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewNurses.html",data=data)

@adminBp.route('/nurses/<Nurse_id>')
def viewNurse(Nurse_id):
    '''
    This is the page that allows the admin to view one Nurse page
    '''
    
    
    mycursor.execute("SELECT name,biography,email,image,phone,gender,birthdate,address,ssn FROM operationsDB.Nurse WHERE ssn="+ Nurse_id)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4],r[5],r[6],r[7],r[8]) for r in myresult]

    return render_template("adminViewNurse.html",data=myresult)

@adminBp.route('/nurses/add')
def addNurses():
    '''
    This is the page that allows the admin to view nurses in a table
    '''
    mycursor.execute("SELECT * FROM operationsDB.Nurse")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }

    return render_template("adminAddNurse.html")

@adminBp.route('/nurses/update/<ssn>')
def updateNurses(ssn):
    '''
    This is the page that allows the admin to view nurses in a table
    '''
    mycursor.execute("SELECT name,biography,email,image,phone,gender,birthdate,address,ssn,superSsn,password,username,salary FROM operationsDB.Nurse WHERE ssn="+ ssn)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12]) for r in myresult]

    return render_template("adminUpdateNurse.html",data=myresult)

#Doctors
@adminBp.route('/doctors')
def viewDoctors():
    '''
    This is the page that allows the admin to view nurses in a table
    '''

    search = request.args.get('search')
    if search == None:
        search = ""
        
    mycursor.execute("SELECT name,biography,email,image,ssn FROM operationsDB.Doctor WHERE name LIKE '%"+search+"%' ORDER BY name ")
   
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4]) for r in myresult]
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewDoctors.html",data=data)

@adminBp.route('/doctors/<doctor_id>')
def viewDoctor(doctor_id):
    '''
    This is the page that allows the admin to view one doctor page
    '''

    mycursor.execute("SELECT name,biography,email,image,phoneNumber,gender,birthdate,address,ssn,username,password FROM operationsDB.Doctor WHERE ssn="+ doctor_id)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4],r[5],r[6],r[7],r[8],r[9],r[10]) for r in myresult]

    return render_template("adminViewDoctor.html",data=myresult)

@adminBp.route('/doctors/add')
def addDoctors():
    '''
    This is the page that allows the admin to view nurses in a table
    '''

    mycursor.execute("SELECT * FROM operationsDB.Doctor")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminAddDoctor.html",data=data)

@adminBp.route('/doctors/update/<ssn>')
def updateDoctor(ssn):
    '''
    This is the page that allows the admin to view nurses in a table
    '''
    mycursor.execute("SELECT name,biography,email,image,phoneNumber,gender,birthdate,address,ssn,username,password FROM operationsDB.Doctor WHERE ssn="+ ssn)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8"),r[4],r[5],r[6],r[7],r[8],r[9],r[10]) for r in myresult]

    return render_template("adminUpdateDoctor.html",data=myresult)

#Rooms
@adminBp.route('/rooms')
def viewRooms():
    '''
    This is the page that allows the admin
    to view rooms in a table
    '''
    search = request.args.get('search')
    type = request.args.get('type')
    if type == 'location':
        mycursor.execute("SELECT * FROM operationsDB.Operation Room WHERE location LIKE '%"+search+"%'")
    elif type == 'id':
        mycursor.execute("SELECT * FROM operationsDB.Operation Room WHERE id LIKE '%"+search+"%'")
    
    
    else :
        mycursor.execute("SELECT * FROM operationsDB.`Operation Room`;")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewRooms.html",data=data)

@adminBp.route('/rooms/add')
def addRooms():
    '''
    This is the page that allows the admin
    to view rooms in a table
    '''

  
    return render_template("adminAddRooms.html")
  

@adminBp.route('/nurses/<Nurse_id>/addOp' ,methods=['POST'])
def addNurseOp(Nurse_id):
    OperationID = request.form['OperationID']
    sql = "INSERT INTO `operationsDB`.`Nurse_has_Operation` (`NurseSSN`, `OperationID`) VALUES (%s, %s);"
    val = (Nurse_id,OperationID)
    mycursor.execute(sql,val)
    mydb.commit()
    return redirect(url_for('adminBp.viewNurses'))