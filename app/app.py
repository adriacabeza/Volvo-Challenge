from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import os
from os.path import join, dirname, realpath
import faceLoginLogin
from werkzeug.security import generate_password_hash
from models.user import User
from flask import Flask, jsonify, Response, redirect, url_for, request, session, abort, render_template
from flask_login import LoginManager, UserMixin, \
login_required, login_user, logout_user, current_user 
import json


mongo_uri = os.environ.get("MONGODB_URI", "mongodb://heroku_xv3vfwld:l3f3d2fv550d1akktp8m9uqj8e@ds119380.mlab.com:19380/heroku_xv3vfwld")

client = MongoClient(mongo_uri)
db = client['heroku_xv3vfwld']

app = Flask(__name__, template_folder='templates/')
app.config['JSON_AS_ASCII'] = False
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'STARTHACKbaby'
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


@app.route('/')
def index():
	return render_template('splash.html',params=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		if current_user.owner:
			return redirect('/dashboard')
		else:
			return redirect('/home')
	if request.method == 'POST':
		username = request.form['name']
		password = request.form['password']
		user_json = db['users'].find_one({"_id": username})
		if user_json is None or not User.validate_login(user_json['password'],password):
			return redirect('/login')
		user = User(user_json['_id'],user_json['email'],user_json['owner'])
		login_user(user)
		nextPage = ''
		if current_user.owner:	
			nextPage = '/dashboard'
		else:
			nextPage = '/home'
		return redirect(nextPage)
	return render_template('login.html',params=None)


@lm.user_loader
def load_user(username):
	u = db['users'].find_one({"_id": username})
	if not u:
		return None
	return User(u['_id'], u['email'], u['owner'])


@app.route('/home')
@login_required
def home():
	return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
	if current_user.owner:
		c = list(db['crashes'].find())
		for cr in c:
			cr['_id'] = int(cr['_id'])
		return render_template('/Dashboard.html', crashes = c)
	else:
		return redirect('/home')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@app.route('/api/users')
def getUsers():
	users = db['users'].find()
	return jsonify(list(users))

@app.route('/signup', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'GET':
		return render_template('registration.html',params=None)
	if request.method == 'POST':
		selfie = request.files['selfie']
		licen = request.files['license']
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		owner = False
		pass_hash = generate_password_hash(password, method='pbkdf2:sha256')
		if faceLoginLogin.registerUser(selfie, licen):
			print("Photos matched!")
			try:
				db['users'].insert({"_id": name, "password": pass_hash, "email": email, "owner": False})
				print ("User created.")
				userJson = db['users'].find_one({"_id": name})
				user = User(userJson['_id'], userJson['email'], userJson['owner'])
				login_user(user)
				return redirect("/home")
			except DuplicateKeyError:
				print ("User already present in DB.")
		else:
			print("Photos didn't match")
		return render_template('registration.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8081))
	app.run(host='0.0.0.0', port=port, debug =True)
	
	
	



#if __name__ == '__init__':
#ficar initial stuff
