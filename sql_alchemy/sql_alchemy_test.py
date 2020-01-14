from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Db Access Config -> DIALECT+DRIVER://USER:PASSWORD@HOST/DB_NAME?SETTING
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/test?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True # Debug on
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'supersecret'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'travel_user'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}
    user_id = db.Column(db.String(100), primary_key=True, unique=True)
    created_at = db.Column(db.DateTime)

db.create_all()