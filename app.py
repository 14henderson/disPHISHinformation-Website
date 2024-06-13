import sqlite3, json, os, datetime
from flask import Flask, render_template, redirect, send_file, Response, request

app = Flask(__name__)
app.secret_key = 'Not so secret key'    #Not doing sessions so probably doesn't matter



#---------Homepage---------#
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')







#@app.route('/', methods=['POST'])
#def login():
# DBCONN = DBCOnnection()
# usersDatabase = UsersDB(DBCONN)
# if 'usernames' in session:
#     session.pop('usernames', None)
# username = request.form[('username')]
# password = request.form[('password')]
# if usersDatabase.authenticate(username, password) == False:
#     DBCONN.close()
#     return render_template('index.html', message="Incorrect username or password")
# elif usersDatabase.getUserBanned(username) == True:
#     DBCONN.close()
#     return render_template('index.html', message="User is currently banned")
# else:
#     session['usernames'] = username
#     if usersDatabase.getUserPriv(username) == 1:
#         DBCONN.close()
#         return redirect("/admin")
#     else:
#         DBCONN.close()
#         return redirect('/groups/home')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)
	
