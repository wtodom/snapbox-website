from flask import Flask, request, session, g, redirect, url_for, \
	 abort, render_template, flash

# Config
DEBUG = True

# Create app
app = Flask(__name__)

# Define routes
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/goals")
def goals():
	return render_template("goals.html")

@app.route("/downloads")
def downloads():
	return render_template("downloads.html")

@app.route("/team")
def team():
	return render_template("team.html")

@app.route("/deliverables")
def deliverables():
	return render_template("deliverables.html")

# Run it.
if __name__ == "__main__":
	app.run()
