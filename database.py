#initates the database file

import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

#cur.execute("INSERT INTO posts (title, content, previewText) VALUES (?, ?, ?)", ('test', 'test', 'test'))

#this will need to be altered before the website goes live  ssss
cur.execute("INSERT INTO users (fullname, username, password, level) VALUES (?, ?, ?, ?)", ('George Vengrovski', 'gibonfrog', 'admin', '0'))

connection.commit()
connection.close()