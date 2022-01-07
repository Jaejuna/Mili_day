from flask import Flask, request, render_template, jsonify
from datetime import datetime
from sqlalchemy import create_engine, text

app = Flask(__name__) 

app.route('/main', methods = ['GET'])
def sign_up():
    user = request.body
    response = {
    	'email'    : user['email'],
        'password' : user['password']
    }
    return jsonify(response), 200	

@app.route('/') 
def hello(): 
    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('index.html', date_time=date_time)


    
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port='8000', debug=True)
