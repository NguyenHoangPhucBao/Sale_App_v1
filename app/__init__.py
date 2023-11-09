from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import hashlib

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://root:%s@localhost/sale_db?charset=utf8mb4"
        % quote("Phucb@(0000)nhpb")
)
app.secret_key = "FGYFYUGYUtyufasfdg#Gv^r6sadfa235tfdg345fg34"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app=app)
login = LoginManager(app=app)


def encrypt(password):
    return str(hashlib.md5(password.encode("utf-8")).hexdigest())
