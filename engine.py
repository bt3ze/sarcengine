import os
from flask import Flask, url_for, render_template, request,session
import jinja2

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def engine():
    return render_template('home.html',user='me')

@app.route('/hello')
def hello():
    return "hello"
