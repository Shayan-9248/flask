from blog import db
from datetime import datetime



class User(db.Model):
	id = db.Column(db.integer, primary_key=True)
	username = db.Column(db.String(30), unique=True, nullable=False)
	email = db.Column(db.String(67), unique=True, nullable=False)
	password = db.Column(db.String(70), nullable=False)
	posts = db.relationshop('Post', backref='author', lazy=True)

	def __repr__(self):
		return f'{self.__class__.__name__}({self.id} - {self.username})'



class Post(db.Model):
	id = db.Column(db.integer, primary_key=True)
	title = db.Column(db.String(77), nullable=False)
	date = db.Column(db.DateTime, default=datetime.now, nullable=False)
	body = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f'{self.__class__.__name__}({self.id} - {self.title[:27]} - {self.date})'