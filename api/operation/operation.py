from flask import Flask,Blueprint, redirect, url_for, request,render_template
# mycursor = mydb.cursor()
operationBp = Blueprint('operationBp', __name__, template_folder='templates',static_folder='static')

@operationBp.route('/add' ,methods=['POST'])
def addOperation():
    #TODO
    #     
    return("Test")

@operationBp.route('/get' ,methods=['GET'])
def getOperation():
    #TODO
    #     
    return("Test")

@operationBp.route('/update' ,methods=['POST'])
def updateOperation():
    #TODO
    #     
    return("Test")

@operationBp.route('/delete' ,methods=['POST'])
def deleteOperation():
    #TODO
    #     
    return("Test")
