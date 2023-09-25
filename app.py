# Spencer Lommel
# Aug 26th, 2023
# Fynetrack API v0.2
# PROJECT ENTRYPOINT

import os
from flask import Flask
from models import db, User
from routes import init_routes

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.secret_key = os.urandom(16)

# Set up the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.urandom(16)
app.config["JWT_HEADER_TYPE"] = "Bearer"
jwt = JWTManager(app)


# Connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fynetrack.db'
db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    init_routes(app)
    app.run(debug=True)
