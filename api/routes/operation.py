from routes import app
from routes import mydb

mycursor = mydb.cursor()

@app.route('/operation/add' ,methods=['POST'])
def addOperation():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/operation/get' ,methods=['GET'])
def getOperation():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/operation/update' ,methods=['POST'])
def updateOperation():
    #TODO
    #     
    return(str(mycursor.lastrowid))

@app.route('/operation/delete' ,methods=['POST'])
def deleteOperation():
    #TODO
    #     
    return(str(mycursor.lastrowid))

operation