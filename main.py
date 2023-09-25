# TEST FILE
# USE APP.PY instead

from flask import Flask, jsonify, request
import time

app = Flask(__name__)


@app.post('/login')
def login():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    print(username, password)
    if username == "spencer5949" and password == "Q4mbn112'":
        # time.sleep(5)
        return jsonify(token="testToken2341"), 200
    else:
        return jsonify(error="Invalid username or password"), 401


# Required: fName, username, email, birthday, password
@app.post('/register')
def register():
    print(request.get_json())

    return jsonify(token='newUserToken'), 200


if __name__ == '__main__':
    # Paths to your SSL certificate and private key files
    ssl_cert = '/etc/letsencrypt/live/test-api.fynetrack.com/fullchain.pem'
    ssl_key = '/etc/letsencrypt/live/test-api.fynetrack.com/privkey.pem'

    app.run(host="0.0.0.0", port=8081, ssl_context=(ssl_cert, ssl_key))