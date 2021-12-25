from flask import Flask

app = Flask(__name__)

from routes import doctor
from routes import admin
from routes import nurse
from routes import operation
from routes import room
from routes import equipment

import mysql.connector
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)

mycursor = mydb.cursor()