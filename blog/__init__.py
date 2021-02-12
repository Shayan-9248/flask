from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = '3795beaaf4b8f6ee4a85a0bfc5b9dc3c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
db = SQLAlchemy(app)



from blog import routes