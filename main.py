from flask import Flask
from application.database import db
import os
from dotenv import load_dotenv

app = None

load_dotenv()


def create_app():
    app = Flask(__name__, template_folder="templates")

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban_database.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.app_context().push()

    return app


app = create_app()


# Import all the controllers so they are loaded
from application.controllers import *


if __name__ == '__main__':
    app.run()
