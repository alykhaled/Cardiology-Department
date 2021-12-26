from flask import Flask,Blueprint, redirect, url_for, request,render_template

# mycursor = mydb.cursor()
adminBp = Blueprint('adminBp', __name__, template_folder='templates',static_folder='static')

@adminBp.route('/')
def index():
    return render_template('index.html')