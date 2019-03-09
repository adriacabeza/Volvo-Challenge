from flask import Flask, render_template, redirect, request, session
from faceLogin import faceLogin
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
import os

flask_app = Flask(__name__, template_folder='templates/')
flask_app.config['JSON_AS_ASCII'] = False


login_manager = LoginManager()
login_manager.init_app(flask_app)

login_manager.login_view = 'login'

@flask_app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
#return render_template('index.html',params=None)
		return "<h1>Home Page</h1>"


@flask_app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if faceLogin.detectUser(request.form['image']): 
			session['logged_in'] = True
			redirect('http://www.pornhub.com', code=30)
	else:
		'''
		alert("Login failed, please take another photo")
		'''
		return home()
	return render_template('login.html')

# @flask_app.route('/map')
# def map():


if __name__ == '__main__':
	flask_app.secret_key = os.urandom(12)
	flask_app.run(host='0.0.0.0', port=8081, debug =True)
	

	

#if __name__ == '__init__':
#ficar initial stuff
#to remember to put in every website
# <link rel="shortcut icon" type="image/ico" href="/favicon.ico"/>