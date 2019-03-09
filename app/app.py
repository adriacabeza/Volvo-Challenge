from flask import Flask, render_template, redirect, request
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import os
from os.path import join, dirname, realpath
import faceLoginLogin
from werkzeug.security import generate_password_hash
import pprint


mongo_uri = os.environ.get("MONGODB_URI", "mongodb://heroku_xv3vfwld:l3f3d2fv550d1akktp8m9uqj8e@ds119380.mlab.com:19380/heroku_xv3vfwld")

client = MongoClient(mongo_uri)
db = client['heroku_xv3vfwld']
collection = db['provaVOLVO']

app = Flask(__name__, template_folder='templates/')
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
	return render_template('splash.html',params=None)

@app.route('/login')
def login():
	return render_template('login.html',params=None)

@app.route('/signup', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'GET':
		return render_template('registration.html',params=None)
	if request.method == 'POST':
		selfie = request.files['selfie']
		licen = request.files['license']
		pprint(request)
		if faceLoginLogin.registerUser(selfie, licen):
			try:
				collection.insert({"_id": user, "password": pass_hash})
				print ("User created.")
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
