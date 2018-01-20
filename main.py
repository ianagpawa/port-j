from flask import Flask, render_template, request, redirect, url_for, flash, \
                    make_response, jsonify, session, escape

import random
import string
import hashlib
import re
import json

from string import letters
from functools import wraps


from google.appengine.ext import ndb

import list_of_projects
# from google.appengine.ext import ndb

APP_SECRET = json.loads(open('secrets.json', 'r').read())['app-secret-key']

app = Flask(__name__)
app.secret_key = APP_SECRET

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/projects', methods=['GET'])
def projects():
    projects = [list_of_projects.first, list_of_projects.second, list_of_projects.third,list_of_projects.first, list_of_projects.second, list_of_projects.third,list_of_projects.first, list_of_projects.second, list_of_projects.third,]
    return render_template("projects.html", projects=projects)
