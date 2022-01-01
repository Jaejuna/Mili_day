from flask import Flask, request, render_template, jsonify
from datetime import datetime
from sqlalchemy import create_engine, text

app = Flask(__name__) 

@app.route('/') 
def hello(): 
    now = datetime.now() # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('index.html', date_time=date_time)

@app.route('/hello') 
def hellohtml(): 
    return render_template("test.html") 


#testing POST method & inserting to DB into 'people' table
def create_app(test_config = None):
    app = Flask(__name__)
    app.config.from_pyfile('myenv/config.py')

    database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
    app.database = database

    @app.route('/test', methods = ['POST'])
    def sign_up():
        user = request.body
        user_id = app.database.execute(text("""
                                            INSERT INTO people (
                                            name,
                                            startDate
                                           ) VALUES (
                                            :name,
                                            :startDate
                                           )
                                            """), user).lastrowid

        return "", 200

    return app


#@app.route('/method', methods=['GET', 'POST']) 
#def method(): 
#    if request.method == 'GET': 
#        return "GET으로 전달" 
#    else: 
#        return "POST로 전달" 
    
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port='8000', debug=True)
