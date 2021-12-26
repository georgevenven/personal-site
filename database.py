#initates the database file
#running the database file should update all the 
#entries on the site because all of the stuff should 
#be stored locally as well
import sqlite3

connection = sqlite3.connect('database.db')

htmlfile = open("test1.txt", "r")
print(htmlfile.read())

with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()