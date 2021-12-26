from flask import Flask, render_template, request, url_for, flash, redirect, session, Markup
from werkzeug.exceptions import abort
from flaskext.markdown import Markdown
import markdown
import sqlite3

app = Flask(__name__)
Markdown(app)
app.config['SECRET_KEY'] = '42' #pass secret key through file private on github

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/writings')
def writings():
    return render_template('writings.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/admin2001')
def admin2001():
    return render_template('admin2001.html')
