import json
from flask import Flask
import platform
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'sDsdfdSsh'
os_info = platform.system()
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open('X:/PNU/Web-Python/ST/python-main/SelfWork1/users.json') as f:
    users = json.load(f)
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_PERMANENT'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
