#!/usr/bin/python3
"""flask server"""
from flask import Flask, jsonify
from api.v1.models import db
from api.v1.routes import app_routes




app = Flask(__name__)


db.init_app(app)
app.register_blueprint(app_routes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:amps3300@localhost/proyect_db'



if __name__ == '__main__':
        db.create_all()
        app.run(port=5000, threaded=True, debug=True)
