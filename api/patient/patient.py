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
@patientBp.route('/add' ,methods=['POST'])
def addPatient():
    #TODO
    if request.method == 'POST':
        Operation_Room_ID = request.form['Operation_Room_ID']
        Operation_ID = request.form['Operation_ID']
        sql = "INSERT INTO `operationsDB`.`Operation Room` (`Operation_Room_ID`,`Operation_ID`) VALUES (%s,%s);"
        val = (Operation_Room_ID,Operation_ID)
        mycursor.execute(sql,val)
        mydb.commit()
        print(Operation_Room_ID,Operation_ID)

    return render_template("adminAddRooms.html")


@patientBp.route('/update' ,methods=['POST'])
def updatePatient():
    #TODO
    #     
    return("TestRoom")

@patientBp.route('/delete/' ,methods=['GET'])
def deletePatient():
    
    return render_template("adminViewPatients.html")
   

