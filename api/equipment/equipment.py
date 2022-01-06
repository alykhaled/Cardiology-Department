from flask import Flask,Blueprint, redirect, url_for, request,render_template
# mycursor = mydb.cursor()
import mysql.connector
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)
equipmentBp = Blueprint('equipmentBp', __name__, template_folder='templates',static_folder='static')

@equipmentBp.route('/add' ,methods=['POST'])
def addNurse():
    #TODO
    #     
    return("Test")

@equipmentBp.route('/get' ,methods=['GET'])
def getNurse():
    #TODO
    #     
    return("Test")

@equipmentBp.route('/update' ,methods=['POST'])
def updateNurse():
    #TODO
    #     
    return("Test")



# mycursor = mydb.cursor()

equipmentBp = Blueprint('equipmentBp', __name__, template_folder='templates',static_folder='static')
mycursor = mydb.cursor()
@equipmentBp.route('/')
def doctorIndex():
    '''
    This is the index page for the doctor that view some statics about latest
    operations and patients that are
    waiting for a doctor
    '''

    return render_template("doctorIndex.html")

@equipmentBp.route('/operations')
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

@equipmentBp.route('/operations/add')
def addOperations():
    '''
    This is the page that allows the doctor
    to view and to add a new operation to the database
    using there api
    '''
    return render_template("doctorAddOperation.html")

@equipmentBp.route('/patients')
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

@equipmentBp.route('/nurses')
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

@equipmentBp.route('/rooms')
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

@equipmentBp.route('/add' ,methods=['POST'])
def addEquipment():
    '''
    This is add POST request for the equipment
    that add a new equipment to the database
    '''
    if request.method == 'POST':
        Equipment_Name = request.form['Equipment_Name']
        Equipment_ID = request.form['Equipment_ID']
        Eq_room = request.form['Eq_Room']
        EquipmentModel = request.form['Equipment_Model']
        Eq_Admission_date = request.form['Eq_Admission_date']
        sql = "INSERT INTO `operationsDB`.`Equipment` (`Equipment_Name`, `Equipment_ID`, `Eq_Room`, `Equipment_Model`, `Eq_Admission_date`) VALUES (%s,%s,%s,%s,%s);"
        val = (Equipment_Name,Equipment_ID,Eq_room,EquipmentModel,Eq_Admission_date)
        mycursor.execute(sql,val)
        mydb.commit()

    return render_template("adminAddEquipment.html")

@equipmentBp.route('/get' ,methods=['GET'])
def getDoctor():
    '''
    This is add POST request for the doctor
    that add a new doctor to the database
    '''  
    return("Test")

@equipmentBp.route('/update' ,methods=['PUT'])
def updateEquipment():
    '''
    This is update PUT request for the doctor
    that update a doctor in the database
    '''    
    return("Test")

@equipmentBp.route('/delete/<Equipment_ID>' ,methods=['GET'])
def deleteEquipment(Equipment_ID):
    sql = "DELETE FROM Equipment WHERE Equipment_ID="+Equipment_ID
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewEquipment'))
