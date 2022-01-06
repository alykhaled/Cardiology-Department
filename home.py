from flask import Flask,Blueprint, redirect, url_for, request,render_template

# mycursor = mydb.cursor()
homeBp = Blueprint('homeBp', __name__, template_folder='templates',static_folder='static')

@homeBp.route('/')
def index():
    return render_template("home.html")

@homeBp.route('/Contactus')
def contactus():
    return render_template("Contactus.html")

@homeBp.route('/login', methods=['GET','POST'])
def login_page():
    return render_template("login.html")
    