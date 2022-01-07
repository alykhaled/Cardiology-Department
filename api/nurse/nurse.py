from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector

# mycursor = mydb.cursor()

nurseBp = Blueprint('nurseBp', __name__, template_folder='templates',static_folder='static')
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)
mycursor = mydb.cursor()
mydb.autocommit = True

@nurseBp.route('/add' ,methods=['POST'])
def addNurse():
     
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        ssn = request.form['ssn']
        SuperSSN = request.form['SuperSSN']
        biography = request.form['biography']
        gender = request.form['gender']
        birthdate = request.form['birthdate']
        phone = request.form['phone']
        address = request.form['address']
        image = request.files['image']
        salary=request.form['Salary']
        sql = "INSERT INTO `operationsDB`.`Nurse` (`ssn`, `name`, `birthdate`, `address`, `superSsn`, `salary`, `biography`, `phone`, `gender`,`username`,`email`,`password`,`image`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (ssn,name,birthdate,address,SuperSSN,salary,biography,phone,gender,username,email,password,image.read())
        mycursor.execute(sql,val)
        mydb.commit()

    return redirect(url_for('adminBp.viewNurses'))

@nurseBp.route('/update' ,methods=['POST'])
def updateNurse():
    #TODO
    #     
    return("Test")

@nurseBp.route('/delete/<ssn>' ,methods=['GET'])
def deleteNurse(ssn):
    #TODO
    sql = "DELETE FROM Nurse WHERE ssn="+ssn
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewNurses'))

