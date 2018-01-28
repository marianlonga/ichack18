from flask import Flask, render_template
app = Flask(__name__)


@app.route("/output")
def output():

	food_log = ""
	with open('food_log.json', 'r') as file:
		food_log = file.read()

	return food_log
	#return render_template("index.html", food_log=food_log)


@app.route("/")
def graphs():
	return render_template("index.html")


@app.route("/chart.js")
def chart_js():
	return render_template("chart.js")


@app.route("/chartConfigs.js")
def chart_configs_js():
	return render_template("chartConfigs.js")


#@app.route('/new/assets/<path:path>')
#def catch_all(path):
	#print("path: " + path)
	#full_path = './new/assets/' + path
	#print(full_path)
	#return app.send_static_file(full_path)

if __name__ == "main":
	app.run()

