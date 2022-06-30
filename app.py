from flask import Flask
from flask_restful import Api
from application.database import db

app = None


def create_app():
    app = Flask(__name__, template_folder="templates")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban_database.sqlite3'

    db.init_app(app)
    
    app.app_context().push()  
    
    return app

app = create_app()


# Import all the controllers so they are loaded
from application.controllers import *

if __name__ == '__main__':
    app.run(debug = True)