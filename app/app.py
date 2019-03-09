from flask import Flask, render_template, redirect, request
from pymongo import MongoClient
import os

mongo_uri = os.environ.get("MONGODB_URI", "mongodb://heroku_xv3vfwld:l3f3d2fv550d1akktp8m9uqj8e@ds119380.mlab.com:19380/heroku_xv3vfwld")

client = MongoClient(mongo_uri)
db = client['heroku_xv3vfwld']
collection = db['provaVOLVO']

app = Flask(__name__, template_folder='templates/')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
#  return render_template('index.html',params=None)
	html = "<h1>Home Page</h1>"
	for doc in collection.find():
		html += doc['name'] + '<br>'
	return html

@app.route('/signup')
def signup():
	return render_template('registration.html',params=None)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8081))
	app.run(host='0.0.0.0', port=port, debug =True)
	
	
	



#if __name__ == '__init__':
#ficar initial stuff
