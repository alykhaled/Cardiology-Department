from routes import app
from routes import mydb

mycursor = mydb.cursor()

@app.route('/')
def index():
    mycursor.execute("SHOW TABLES")
    s = ""
    for x in mycursor:
        s += str(x)
        print(x)
    return(str(s))