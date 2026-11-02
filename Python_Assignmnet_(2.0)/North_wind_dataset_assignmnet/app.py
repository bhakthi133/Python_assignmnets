"""
a. Create a Rest API in python using flask which supports the following operations on the
Northwind dataset
1. Insert, update and select on customers
2. Insert, update and select on products
3. Insert, update and select on orders
4. Order history of the given customer
"""
from flask_sqlalchemy import URL
from flask import Flask
from sqlalchemy import SQLAlchemy

app=Flask(__name__)

url=URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Bhak@13",
    host="localhost",
    port=3306,
    database="northwind"
)

app.config["SQLALCHEMY_DATABASE_URI"]=url

db=SQLAlchemy(app)

from sqlalchemy import Text, LargeBinary


class Customer(db.Model):

    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    email_address = db.Column(db.String(50))
    job_title = db.Column(db.String(50))
    business_phone = db.Column(db.String(25))
    home_phone = db.Column(db.String(25))
    mobile_phone = db.Column(db.String(25))
    fax_number = db.Column(db.String(25))
    address = db.Column(Text)
    city = db.Column(db.String(50))
    state_province = db.Column(db.String(50))
    zip_postal_code = db.Column(db.String(15))
    country_region = db.Column(db.String(50))
    web_page = db.Column(Text)
    notes = db.Column(Text)
    attachments = db.Column(LargeBinary)

with app.app_context():
    with db.engine.connect() as connection:
        print("Database connected success") 

@app.route("/customers",methods=["GET"])
def get_customers():
    c=Customer.query.all()




def get_customers():
    c=customers