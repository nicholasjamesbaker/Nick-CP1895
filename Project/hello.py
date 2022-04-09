import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/photos")
def photos():
    images = ["image1.jpg"]
    return render_template("photos.html", images=images)



"""@app.route("/<string:name>")
def hello(name):
    return render_template("index.html", name=request.args.get("name", "world"))
"""
