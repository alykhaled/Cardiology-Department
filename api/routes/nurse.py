from routes import app
from routes import mydb

mycursor = mydb.cursor()

@app.route('/nurse/add' ,methods=['POST'])
def addNurse():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/nurse/get' ,methods=['GET'])
def getNurse():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/nurse/update' ,methods=['POST'])
def updateNurse():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/nurse/delete' ,methods=['POST'])
def deleteNurse():
    #TODO
    #     
    return(str(mycursor.lastrowid))

