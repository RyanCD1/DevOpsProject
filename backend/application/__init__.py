from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

#DB_USER=admin
#DB_PW=XeQkrjLNwQ6qySn
#DB_URL=projectdb.cjmj7j0zzqco.eu-west-1.rds.amazonaws.com
#DB_NAME=users

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:{os.getenv("DB_PW")}@projectdb.cjmj7j0zzqco.eu-west-1.rds.amazonaws.com:3306/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = str(getenv('SECRET_KEY'))
db = SQLAlchemy(app)

from application import routes
