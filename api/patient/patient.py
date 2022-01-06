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
        currentOperation = request.form['currentOperation']
        address = request.form['address']
        gender = request.form['gender']
        Relatives_phone_Number = request.form['Relatives_phone_Number']
        sql = "INSERT INTO `operationsDB`.`Patient` (`ssn`,`name`,`medicalHistory`,`illness`,`bdate`,`phone`,`image`,`username`,`password`,`email`,`currentOperation`,`address`,`gender`,`Relatives_phone_Number`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (ssn,name,medicalHistory,illness,bdate,phone,image.read(),username,password,email,currentOperation,address,gender,Relatives_phone_Number)
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
   

