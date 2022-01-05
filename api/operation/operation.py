from flask import Flask,Blueprint, redirect, url_for, request,render_template
# mycursor = mydb.cursor()
operationBp = Blueprint('operationBp', __name__, template_folder='templates',static_folder='static')
import mysql.connector
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)
mycursor = mydb.cursor()

@operationBp.route('/add' ,methods=['POST'])
def addOperation():
    #TODO
    #     
    return("Test")

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
