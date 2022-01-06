from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector

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
    mycursor.execute("SELECT * FROM operationsDB.Patient")
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

    mycursor.execute("SELECT * FROM operationsDB.Patient")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    data = {
        'message':"data retrieved",
        'rec':myresult,
        'header':row_headers
    }
    return render_template("doctorViewPatients.html",data=data)

@doctorBp.route('/nurses')
def viewNurses():
    '''
    This is the page that allows the doctor
    to view nurses in a table
    '''

    mycursor.execute("SELECT * FROM operationsDB.Patient")
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

    mycursor.execute("SELECT * FROM operationsDB.Patient")
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

@doctorBp.route('/get' ,methods=['GET'])
def getDoctor():
    '''
    This is add POST request for the doctor
    that add a new doctor to the database
    '''  
    return("Test")

@doctorBp.route('/update' ,methods=['PUT'])
def updateDoctor():
    '''
    This is update PUT request for the doctor
    that update a doctor in the database
    '''    
    return("Test")

@doctorBp.route('/delete' ,methods=['POST'])
def deleteDoctor():
    '''
    This is delete request for the doctor
    that delete a doctor from the database
    '''    
    return("Test")
