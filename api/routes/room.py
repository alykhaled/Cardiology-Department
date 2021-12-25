from routes import app
from routes import mydb

mycursor = mydb.cursor()

@app.route('/room/add' ,methods=['POST'])
def addRoom():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/room/get' ,methods=['GET'])
def getRoom():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/room/update' ,methods=['POST'])
def updateRoom():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/room/delete' ,methods=['POST'])
def deleteRoom():
    #TODO
    #     
    return(str(mycursor.lastrowid))

