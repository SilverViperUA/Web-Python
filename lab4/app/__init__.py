import json
from flask import Flask
import platform
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'klchJ89Bch'

os_info = platform.system()
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('X:/PNU/Web-Python/ST/python-main/lab4/users.json') as f:
    users = json.load(f)

from app import views