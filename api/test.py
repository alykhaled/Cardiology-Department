from flask import Flask
import mysql.connector
mydb = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database=""
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/')
def index():
    return("hello world")

if __name__ == '__main__':
    app.run()
