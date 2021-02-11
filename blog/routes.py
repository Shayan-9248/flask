from blog import app
from flask import render_template



@app.route('/')
def routes():
	return render_template('home.html')