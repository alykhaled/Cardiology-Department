from flask import Flask,Blueprint, redirect, url_for, request,render_template
import mysql.connector

mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)
# mycursor = mydb.cursor()
mydb.autocommit = True


roomBp = Blueprint('roomBp', __name__, template_folder='templates',static_folder='static')

mycursor = mydb.cursor()
@roomBp.route('/add' ,methods=['POST'])
def addRoom():
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


@roomBp.route('/update' ,methods=['POST'])
def updateRoom():
    #TODO
    #     
    return("TestRoom")

@roomBp.route('/delete/<Operation_Room_ID>' ,methods=['GET'])
def deleteRoom(Operation_Room_ID):
    #TODO
    sql = "DELETE FROM `Operation Room` WHERE Operation_Room_ID="+Operation_Room_ID
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewRooms'))
   

