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
        Room_Location = request.form['Room_Location']
        sql = "INSERT INTO `operationsDB`.`Operation Room` (`Room_Location`) VALUES ('"+Room_Location+"')"
        print(sql)
        val = (Room_Location)
        mycursor.execute(sql)
        mydb.commit()

    return render_template("adminAddRooms.html")


@roomBp.route('/update' ,methods=['POST','GET'])
def updateRoom(id):
    #TODO
    # 
    if request.method == 'POST':
        Room_Location = request.form['Room_Location']
        sql = "UPDATE `operationsDB`.`Operation Room` SET Operation_Room_ID=%s,Room_Location=%s WHERE Operation_Room_ID="+id
        print(sql)
        val = (Room_Location)
        mycursor.execute(sql)
        mydb.commit()
    redirect(url_for('adminBp.viewRooms'))
    
    

@roomBp.route('/delete/<Operation_Room_ID>' ,methods=['GET'])
def deleteRoom(Operation_Room_ID):
    #TODO
    sql = "DELETE FROM `Operation Room` WHERE Operation_Room_ID="+Operation_Room_ID
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewRooms'))
   

