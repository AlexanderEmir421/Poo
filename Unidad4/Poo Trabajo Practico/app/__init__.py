from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def CrearServidor():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    db.init_app(app)
    
    with app.app_context():
        pass
    
    return app
