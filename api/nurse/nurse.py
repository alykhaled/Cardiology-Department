from flask import Flask,Blueprint, redirect, url_for, request,render_template
# mycursor = mydb.cursor()

nurseBp = Blueprint('nurseBp', __name__, template_folder='templates',static_folder='static')

@nurseBp.route('/add' ,methods=['POST'])
def addNurse():
    #TODO
    #     
    return("Test")

@nurseBp.route('/get' ,methods=['GET'])
def getNurse():
    #TODO
    #     
    return("Test")

@nurseBp.route('/update' ,methods=['POST'])
def updateNurse():
    #TODO
    #     
    return("Test")

@nurseBp.route('/delete' ,methods=['POST'])
def deleteNurse():
    #TODO
    #     
    return("Test")

