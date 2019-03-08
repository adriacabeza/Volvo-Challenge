from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder='templates/')
app.config['JSON_AS_ASCII'] = False

@flask_app.route('/')
def index():
#  return render_template('index.html',params=None)
	return "<h1>Home Page</h1>"

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 8081))
	app.run(host='0.0.0.0', port=port, debug =True)


#if __name__ == '__init__':
#ficar initial stuff
