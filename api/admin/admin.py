from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector
from base64 import b64encode

adminBp = Blueprint('adminBp', __name__, template_folder='templates',static_folder='static')
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)
mycursor = mydb.cursor()

@adminBp.route('/')
def index():
    return render_template('index.html')

@adminBp.route('/operations')
def viewOperations():
    '''
    This is the page that allows the admin
    to view and to add a new operation to the database
    using there api
    '''
    mycursor.execute("SELECT * FROM operationsDB.Operation")
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

@adminBp.route('/equipment/add')
def addEquipment():
    '''
    This is the page that allows the admin
    to view and to add a new equipment to the database
    using there api
    '''

    return render_template("adminAddEquipment.html")


@adminBp.route('/patients')
def viewPatient():
    '''
    This is the page that allows the admin
    to view patient in a table
    '''

    mycursor.execute("SELECT name,phone,currentOperation,illness,bdate FROM operationsDB.Patient")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewPatients.html",data=data)

@adminBp.route('/nurses')
def viewNurses():
    '''
    This is the page that allows the admin to view nurses in a table
    '''

    mycursor.execute("SELECT ssn,name,birthdate,address,currentOperation,superSsn,salary,biography,phone,gender,username,email,password FROM operationsDB.Nurse")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewNurses.html",data=data)

@adminBp.route('/nurses/add')
def addNurses():
    '''
    This is the page that allows the admin to view nurses in a table
    '''

    return render_template("adminAddNurse.html")

@adminBp.route('/patients/add')
def addPatients():
    '''
    This is the page that allows the admin to view nurses in a table
    '''
    print("test")
    return render_template("adminAddPatient.html")


@adminBp.route('/doctors')
def viewDoctors():
    '''
    This is the page that allows the admin to view nurses in a table
    '''

    mycursor.execute("SELECT name,biography,email,image FROM operationsDB.Doctor;")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    
    # tesst = b64encode(myresult[0][3])
    myresult = [(r[0],r[1],r[2],b64encode(r[3]).decode("utf-8")) for r in myresult]
    # print(myresult)
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewDoctors.html",data=data)

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

@adminBp.route('/rooms')
def viewRooms():
    '''
    This is the page that allows the admin
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
    return render_template("adminViewRooms.html",data=data)

@adminBp.route('/rooms/add')
def addRooms():
    '''
    This is the page that allows the admin
    to view rooms in a table
    '''

  
    return render_template("adminAddRooms.html")
  
@adminBp.route('/equipment')
def viewEquipment():
    '''
    This is the page that allows the admin
    to view equipment in a table
    '''

    mycursor.execute("SELECT * FROM operationsDB.Equipment")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("adminViewEquipment.html",data=data)

