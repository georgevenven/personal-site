#initates the database file
#running the database file should update all the 
#entries on the site because all of the stuff should 
#be stored locally as well
import sqlite3
import os
import time

#parses the various infos from filename
def parsing(filename):
    title = ''
    topic = ''
    previewText = ''
    j = 0 
    for i in range(len(filename)):
        if filename[i] != '~':
            title = title + filename[i]
        else: 
            i = i+1   
            if filename[i] != '~':
                for j in range(len(filename)):
                    if j+i < len(filename):
                        if filename[j+i] != '~':
                            topic = topic + filename[j+i]
                        else:
                            for z in range(len(filename)):
                                if z+i+j < len(filename):
                                    if filename[j+i+z] != '.':
                                        previewText = previewText + filename[j+z+i]
                                    else:
                                        break
            break
    #the computational complexity do be hitting LOL
    return topic, title, previewText

def dateParser(date):
    newDate =''

    for x in range(len(date)): 
        if x > 3 and x < 10:
            newDate = newDate + date[x]
        if x > 18:
            newDate = newDate + date[x]

    return newDate


connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cwd = os.getcwd()
files = os.listdir(cwd + "/posts/")
os.chdir(cwd + '/posts/')

for i in files:
    if i.endswith('.txt'):
        htmlfile = open(i, "r")
        content = (htmlfile.read())
        returnTupel = parsing(i)
        date = time.ctime(os.path.getctime(i)) # gets creation date of file, may be problematic when deplpyed on server 
        date = dateParser(date)
        cur.execute("INSERT INTO posts (title, content, topic, created, previewText) VALUES (?, ?, ?, ?, ?)", (returnTupel[1], content, returnTupel[0], date, returnTupel[2]))

connection.commit()
connection.close()