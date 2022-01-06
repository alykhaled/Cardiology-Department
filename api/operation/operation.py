from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector

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
    #TODO
    if request.method == 'POST':
        id = request.form['id']
        operationName = request.form['operationName']
        patientId = request.form['patientId']
        doctorId = request.form['doctorId']
        roomId = request.form['roomId']
        date = request.form['date']
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        sql = "INSERT INTO `operationsDB`.`Operation` (`id`,`operationName`,`patientId`,`doctorId`,`roomId`,`date`,`startTime`,`endTime`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (id,operationName,patientId,doctorId,roomId,date,startTime,endTime)
        mycursor.execute(sql,val)
        mydb.commit()
        # print(id,operationName,patientId,doctorId,roomId,date,startTime,endTime)
    return redirect(url_for('adminBp.viewOperations'))


@operationBp.route('/get' ,methods=['GET'])
def getOperation():
    #TODO
    #     
    return("Test")

@operationBp.route('/update' ,methods=['POST'])
def updateOperation():
    #TODO
    #     
    return("Test")

@operationBp.route('/delete/<operation_id>' ,methods=['GET'])
def deleteOperation(operation_id):
    sql = "DELETE FROM Operation WHERE id="+operation_id
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewOperations'))
