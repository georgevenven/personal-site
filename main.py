from flask import Flask, render_template, request, url_for, flash, redirect, session, Markup
from werkzeug.exceptions import abort
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '42' #pass secret key through file private on github

#database functions 
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

def dataBasePostRetrieval(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    connection.close()
    if post is None:
        abort(404)
    return post

def getAllPosts():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return posts

#page functions 
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/writings')
def writings():
    posts = getAllPosts()
    return render_template('writings.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/admin2001')
def admin2001():
    return render_template('admin2001.html')

@app.route('/<int:post_id>')
def post(post_id):
    temp = dataBasePostRetrieval(post_id)
    post = (temp[4])
    title = (temp[2])
    return render_template('post.html', post=post, title=title)
