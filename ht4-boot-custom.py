# hello with templates, version 4  

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask import request
from flask import current_app
from raspi_temp import CPUTemp

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
	

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500


@app.route("/")
def index():
	return render_template('ht4-index.html', curApp = current_app.name)


@app.route("/img")
def img():
	return '<img src="/static/img/winter.jpg">'

@app.route("/temp")
def temperature():
	with CPUTemp() as cpu_temp:
		temp_c = round(cpu_temp.get_temp(), 1)
		temp_f = round(cpu_temp.get_temp_in_f(), 1)
	return render_template('ht4-temp.html', c_temp = temp_c, f_temp = temp_f)


@app.route("/req")
def req():
	agnt = request.headers.get('User-Agent')
	return render_template('ht4-user.html', uName=agnt)


@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
	return render_template('ht4-user.html', uName=name)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
