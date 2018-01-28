from flask import Flask, render_template
app = Flask(__name__)


@app.route("/output")
def output():

	food_log = ""
	with open('food_log.json', 'r') as file:
		food_log = file.read()

	return food_log
	#return render_template("index.html", food_log=food_log)


@app.route("/graphs")
def graphs():
	return render_template("index.html")


@app.route("/chart.js")
def chart_js():
	return render_template("chart.js")

@app.route("/chartConfigs.js")
def chart_configs_js():
	return render_template("chartConfigs.js")


if __name__ == "main":
	app.run()

