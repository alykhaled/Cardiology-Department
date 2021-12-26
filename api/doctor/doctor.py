from flask import Flask,Blueprint, redirect, url_for, request,render_template

# mycursor = mydb.cursor()
doctorBp = Blueprint('doctorBp', __name__, template_folder='templates',static_folder='static')

@doctorBp.route('/add' ,methods=['POST'])
def addDoctor():
    #TODO
    #     
    return("Test")

@doctorBp.route('/get' ,methods=['GET'])
def getDoctor():
    #TODO
    #     
    return("Test")

@doctorBp.route('/update' ,methods=['POST'])
def updateDoctor():
    #TODO
    #     
    return("Test")

@doctorBp.route('/delete' ,methods=['POST'])
def deleteDoctor():
    #TODO
    #     
    return("Test")
