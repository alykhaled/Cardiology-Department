from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector
from Google import create_service
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB",autocommit=True
)
mydb.autocommit = True
# mycursor = mydb.cursor()

operationBp = Blueprint('operationBp', __name__, template_folder='templates',static_folder='static')

mycursor = mydb.cursor()
@operationBp.route('/add' ,methods=['POST'])
def addOperation():
    

    if request.method == 'POST':
        operationName = request.form['operationName']
        patientId = request.form['patientId']
        doctorId = request.form['doctorId']
        roomId = request.form['roomId']
        date = request.form['date']
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        sql = "INSERT INTO `operationsDB`.`Operation` (`operationName`,`patientId`,`doctorId`,`roomId`,`date`,`startTime`,`endTime`) VALUES (%s,%s,%s,%s,%s,%s,%s);"

        val = (operationName,patientId,doctorId,roomId,date,startTime,endTime)
        mycursor.execute(sql,val)
        mydb.commit()
    return redirect(url_for('adminBp.viewOperations'))


@operationBp.route('/update/<id>' ,methods=['POST'])
def updateOperation(id):
    #TODO
    #  
    if request.method == 'POST':
        operationName = request.form['operationName']
        patientId = request.form['patientId']
        doctorId = request.form['doctorId']
        roomId = request.form['roomId']
        date = request.form['date']
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        sql = "UPDATE `operationsDB`.`Operation` SET operationName=%s,patientId=%s,doctorId=%s,roomId=%s,date=%s,startTime=%s,endTime=%s WHERE id="+id
        val = (operationName,patientId,doctorId,roomId,date,startTime,endTime)
        mycursor.execute(sql,val)
        mydb.commit()
    return redirect(url_for('adminBp.viewOperations'))   
    

@operationBp.route('/delete/<operation_id>' ,methods=['GET'])
def deleteOperation(operation_id):
    sql = "DELETE FROM Operation WHERE id="+operation_id
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewOperations'))
