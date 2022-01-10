from flask import Flask,Blueprint, redirect, url_for, request,render_template, session
import mysql.connector
from Google import create_service
import os
import datetime
import os.path
from flask_cors import CORS, cross_origin

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

mydb = mysql.connector.connect(
    host='34.71.50.183',
    user="root",
    port=3306,
    passwd="alykhaled123",
    database="operationsDB",autocommit=True
)
mydb.autocommit = True
# mycursor = mydb.cursor()

operationBp = Blueprint('operationBp', __name__, template_folder='templates',static_folder='static')

CLIENT_SECRET_FILE = "client_secret_240695600096-ndnm8sahb9f9p117913u6ugkhak9rlq1.apps.googleusercontent.com.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ['https://www.googleapis.com/auth/calendar']

mycursor = mydb.cursor()
@operationBp.route('/add' ,methods=['POST'])
def addOperation():

    if request.method == 'POST':
        operationName = request.form['operationName']
        patientId = request.form['patientId']
        doctorId = ""
        print(session.get("accountType"))
        if session.get("accountType") == "doctor":
            doctorId = session.get("id")
        else:
            doctorId = request.form['doctorId']
        roomId = request.form['roomId']
        date = request.form['date']
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        sql = "INSERT INTO `operationsDB`.`Operation` (`operationName`,`patientId`,`doctorId`,`roomId`,`date`,`startTime`,`endTime`) VALUES (%s,%s,%s,%s,%s,%s,%s);"

        val = (operationName,patientId,doctorId,roomId,date,startTime,endTime)
        mycursor.execute(sql,val)
        mydb.commit()
        
        mycursor.execute("SELECT name FROM Patient WHERE ssn = " + patientId)
        patientName = mycursor.fetchall()[0][0]
        
        mycursor.execute("SELECT Room_Location FROM `Operation Room` WHERE Operation_Room_ID = " + roomId)
        roomLocation = mycursor.fetchall()[0][0]

        if session.get("accountType") == 'doctor':
            creds = None
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if creds:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())

                try:
                    service = build('calendar', 'v3', credentials=creds)
                    event = {
                    'summary': operationName + ' Operation',
                    'location': roomLocation,
                    'description': operationName + ' Operation for ' + patientName,
                    'start': {
                        'dateTime': date + 'T' + startTime + ':00+02:00',
                    },
                    'end': {
                        'dateTime': date + 'T' + endTime + ':00+02:00',
                    }
                    }
                    print(date + 'T' + startTime + ':00+02:00')
                    print(date + 'T' + endTime + ':00+02:00')
                    event = service.events().insert(calendarId='primary', body=event).execute()
                    print ('Event created: %s' % (event.get('htmlLink')))
                except HttpError as error:
                    print ('An error occurred: %s' % error)
                
    return redirect(url_for('adminBp.viewOperations'))


@operationBp.route('/update/<id>' ,methods=['POST'])
def updateOperation(id):
    #TODO
    #  
    if request.method == 'POST':
        operationName = request.form['operationName']
        patientId = request.form['patientId']
        doctorId = request.form['doctorId']
        roomId = request.form['roomId']
        date = request.form['date']
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        sql = "UPDATE `operationsDB`.`Operation` SET operationName=%s,patientId=%s,doctorId=%s,roomId=%s,date=%s,startTime=%s,endTime=%s WHERE id="+id
        val = (operationName,patientId,doctorId,roomId,date,startTime,endTime)
        mycursor.execute(sql,val)
        mydb.commit()
    
    if session.get("accountType") == "doctor":
        return redirect(url_for('doctorBp.viewOperations'))   
    else:
        return redirect(url_for('adminBp.viewOperations'))   
    

@operationBp.route('/delete/<operation_id>' ,methods=['GET'])
def deleteOperation(operation_id):
    sql = "DELETE FROM Operation WHERE id="+operation_id
    # val = (int(operation_id))
    mycursor.execute(sql)
    mydb.commit()
    return redirect(url_for('adminBp.viewOperations'))
