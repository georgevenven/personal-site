#initates the database file
#running the database file should update all the 
#entries on the site because all of the stuff should 
#be stored locally as well
import sqlite3
import os

def parsing(filename):
    title = ''
    topic = ''
    for i in range(len(filename)):
        if filename[i] != ',':
            title = title + filename[i]
        else: 
            i = i+1 
            for j in range(len(filename)):
                if j+i < len(filename):
                    if filename[j+i] != '.':
                        topic = topic + filename[j+i]
                    else:
                        break
            break

    return topic, title


connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cwd = os.getcwd()
files = os.listdir(cwd + "/posts/")
os.chdir(cwd + '/posts/')

for i in files:
    htmlfile = open(i, "r")
    content = (htmlfile.read())
    returnTupel = parsing(i)
    cur.execute("INSERT INTO posts (title, content, topic) VALUES (?, ?, ?)", (returnTupel[1], content, returnTupel[0]))

connection.commit()
connection.close()