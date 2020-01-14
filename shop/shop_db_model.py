from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Db Access Config -> DIALECT+DRIVER://USER:PASSWORD@HOST/DB_NAME?SETTING
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/shop_db?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True # Debug on
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'supersecret'

db = SQLAlchemy(app)

class CatgoryInfo(db.Model):
    __tablename__ = 'category_info_t'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}
    c_no = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(50), nullable=False)

class ProductInfo(db.Model):
    __tablename__ = 'product_info_t'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}
    c_no = db.Column(db.Integer, db.ForeignKey(CatgoryInfo.c_no), nullable=False)
    p_no = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(50), nullable=False)
    p_price = db.Column(db.Integer, nullable=False)
    p_stock = db.Column(db.Integer)
    p_expired = db.Column(db.DateTime)

db.create_all()