# hello with templates, version 3

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/index")
def index():
	return render_template('ht3-index.html')
	
@app.route('/user/<name>')
def user(name):
	return render_template('ht3-user.html', uName=name)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
