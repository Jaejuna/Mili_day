from flask import Flask, request, jsonify

app = Flask(__name__)

app.route('/sign_up', methods = ['POST'])
def sign_up():
    user = request.body
    response = {
    	'email'    : user['email'],
        'password' : user['password']
    }
    return jsonify(response), 200	

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port='8000', debug=True)