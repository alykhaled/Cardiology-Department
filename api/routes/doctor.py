from routes import app
from routes import mydb

mycursor = mydb.cursor()

@app.route('/doctor/add' ,methods=['POST'])
def addDoctor():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/doctor/get' ,methods=['GET'])
def getDoctor():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/doctor/update' ,methods=['POST'])
def updateDoctor():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/doctor/delete' ,methods=['POST'])
def deleteDoctor():
    #TODO
    #     
    return(str(mycursor.lastrowid))

