import imghdr
import os
import sys
from waitress import serve

from flask import Flask, render_template, g, redirect, request, session, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_PATH'] = 'static/images'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)
    serve(app, host='0.0.0.0', port=80)
