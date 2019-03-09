from flask import Flask, render_template, redirect, request
from faceLogin import faceLogin


flask_app = Flask(__name__, template_folder='templates/')
flask_app.config['JSON_AS_ASCII'] = False

@flask_app.route('/')
def index():
	faceLogin.detectUser()
#return render_template('index.html',params=None)
	return "<h1>Home Page</h1>"

if __name__ == '__main__':
	flask_app.run(host='0.0.0.0', port=8081, debug =True)
	


#if __name__ == '__init__':
#ficar initial stuff
