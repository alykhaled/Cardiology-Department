from flask import Flask
from admin.admin import adminBp
from doctor.doctor import doctorBp
from nurse.nurse import nurseBp
from operation.operation import operationBp
from room.room import roomBp
from equipment.equipment import equipmentBp
from home.home import homeBp
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)

app.register_blueprint(homeBp)
app.register_blueprint(adminBp,url_prefix='/admin')
app.register_blueprint(doctorBp,url_prefix='/doctor')
app.register_blueprint(nurseBp,url_prefix='/nurse')
app.register_blueprint(operationBp,url_prefix='/operation')
app.register_blueprint(equipmentBp,url_prefix='/equipment')
app.register_blueprint(roomBp,url_prefix='/room')

if __name__ == '__main__':
    app.run(debug=True)
