from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import os
from os.path import join, dirname, realpath
import faceLoginLogin
from werkzeug.security import generate_password_hash
from models.user import User
from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask_login import LoginManager, UserMixin, \
login_required, login_user, logout_user 


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

@app.route('/login')
def login():
	return render_template('login.html',params=None)

@lm.user_loader
def load_user(username):
	u = db['users'].find_one({"_id": username})
	if not u:
		return None
	return User(u['_id'])

@app.route('/write', methods=['GET', 'POST'])
@login_required
def write():
	return "<h1>HELLO</h1>"

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
		pass_hash = generate_password_hash(password, method='pbkdf2:sha256')
		if faceLoginLogin.registerUser(selfie, licen):
			try:
				db['users'].insert({"_id": name, "password": pass_hash, "email": email})
				print ("User created.")
				user = db['users'].find_one({"_id": name})
				login_user(User(name))
				return redirect("/")
			except DuplicateKeyError:
				print ("User already present in DB.")
		else:
			print("WRONG PERSON")
		return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8081))
	app.run(host='0.0.0.0', port=port, debug =True)
	
	
	



#if __name__ == '__init__':
#ficar initial stuff
