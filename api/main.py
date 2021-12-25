from routes import app
from flask import Flask
import mysql.connector
mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB"
)

mycursor = mydb.cursor()

if __name__ == '__main__':
    app.run()
