from personal_site import app
from json import load, dump # parse and add json data
import urllib.request
from flask import render_template, request, make_response, redirect, session

# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('flask_index.html')