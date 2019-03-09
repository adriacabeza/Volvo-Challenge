from flask import Flask, render_template, redirect, request
from pymongo import MongoClient
import os
from os.path import join, dirname, realpath
from src.faceLogin.faceLogin.py import registerUser 

mongo_uri = os.environ.get("MONGODB_URI", "mongodb://heroku_xv3vfwld:l3f3d2fv550d1akktp8m9uqj8e@ds119380.mlab.com:19380/heroku_xv3vfwld")

client = MongoClient(mongo_uri)
db = client['heroku_xv3vfwld']
collection = db['provaVOLVO']

app = Flask(__name__, template_folder='templates/')
app.config['JSON_AS_ASCII'] = False

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
	return render_template('index.html',params=None)

@app.route('/signup', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'GET':
		return render_template('registration.html',params=None)
	if request.method == 'POST':
		selfie = request.files['selfie']
		licen = request.files['license']
		if registerUser(selfie, licen):
			print("SAME PERSON BABY")
		else:
			print("WRONG PERSON")
		return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8081))
	app.run(host='0.0.0.0', port=port, debug =True)
	
	
	



#if __name__ == '__init__':
#ficar initial stuff
