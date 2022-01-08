from flask import Flask, request, render_template, jsonify
from datetime import datetime
from sqlalchemy import create_engine, text

app = Flask(__name__) 

@app.route('/') 
def hello(): 
    return render_template('index.html')
    
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port='8000', debug=True)
