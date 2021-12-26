from flask import Flask,Blueprint, redirect, url_for, request,render_template

# mycursor = mydb.cursor()

roomBp = Blueprint('roomBp', __name__, template_folder='templates',static_folder='static')


@roomBp.route('/add' ,methods=['POST'])
def addRoom():
    #TODO
    #     
    return("TestRoom")

@roomBp.route('/get' ,methods=['GET'])
def getRoom():
    #TODO
    #     
    return("TestRoom")

@roomBp.route('/update' ,methods=['POST'])
def updateRoom():
    #TODO
    #     
    return("TestRoom")

@roomBp.route('/delete' ,methods=['POST'])
def deleteRoom():
    #TODO
    #     
    return("TestRoom")

