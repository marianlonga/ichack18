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


if __name__ == "main":
	app.run()

