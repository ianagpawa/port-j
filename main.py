from flask import Flask, render_template, request, redirect, url_for, flash, \
                    make_response, jsonify, session, escape

import random
import string
import hashlib
import re
import json

from string import letters
from functools import wraps

# from google.appengine.ext import ndb

APP_SECRET = json.loads(open('secrets.json', 'r').read())['app-secret-key']

app = Flask(__name__)
app.secret_key = APP_SECRET

print APP_SECRET
