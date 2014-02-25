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

# Run it.
if __name__ == "__main__":
	app.run()
