from flask import Flask,Blueprint, redirect, url_for, request,render_template
# mycursor = mydb.cursor()

equipmentBp = Blueprint('equipmentBp', __name__, template_folder='templates',static_folder='static')

@equipmentBp.route('/add' ,methods=['POST'])
def addNurse():
    #TODO
    #     
    return("Test")

@equipmentBp.route('/get' ,methods=['GET'])
def getNurse():
    #TODO
    #     
    return("Test")

@equipmentBp.route('/update' ,methods=['POST'])
def updateNurse():
    #TODO
    #     
    return("Test")

@equipmentBp.route('/delete' ,methods=['POST'])
def deleteNurse():
    #TODO
    #     
    return("Test")

