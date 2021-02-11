from flask import Flask
from flask_sqlachemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
db = SQLAlchemy(app)



from blog import routes