from flask import Flask, request, render_template

app = Flask(__name__) 

@app.route('/') 
def hello(): 
    return 'Hello, World!' 

@app.route('/hello') 
def hellohtml(): 
    return render_template("test.html") 

@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': 
        return "GET으로 전달" 
    else: 
        return "POST로 전달" 
    
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port='8000', debug=True)
