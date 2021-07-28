#!/usr/bin/python3
"""flask server"""
from flask import Flask, jsonify
from api.v1.routes import app_routes
from api.v1.models import *
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.register_blueprint(app_routes)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)




if __name__ == '__main__':
        db.create_all()
        app.run(port=5000, threaded=True, debug=True)
