# hello with templates, version 4
# custom error pages

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.errorhandle(404)
def page_not_found(e):
	return render_template('404.html'), 404
	
@app.errorhandle(500)
	return render_template('500.html'), 500

@app.route("/")
def index():
	return render_template('ht4-index.html')
	
@app.route('/user/<name>')
def user(name):
	return render_template('ht4-user-boot.html', uName=name)
	


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
