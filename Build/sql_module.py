#Placeholder

import mysql.connector


class sqlSession:
    discordDB = None
    SQLCursor = None

    #Database Init
    def dbInit(): 
        discordDB = mysql.connector.connect(host="127.0.0.1", user="root", password="admin")
        SQLCursor = discordDB.cursor()
        SQLCursor.execute("SHOW DATABASES")

        print ("Current SQL databases:")
        for x in SQLCursor:
            print(x)

        try:
            discordDB = mysql.connector.connect(host="127.0.0.1", user="root", password="admin", database= "discord_db")
            print ("DB link established")
        except mysql.connector.Error as err:
            SQLCursor.execute("CREATE DATABASE discord_db")
            discordDB = mysql.connector.connect(host="127.0.0.1", user="root", password="admin", database= "discord_db")
            print("Discord database not found, created new database, link established")

        SQLCursor = discordDB.cursor()

        #init default tables
        SQLCursor.execute("SHOW TABLES")
        results = SQLCursor.fetchall()
        for x in results:
            print (x)

        if ('words',) in results:
            print ("words tables initialized")
        else:
            SQLCursor.execute("CREATE TABLE words (word VARCHAR(255), userid VARCHAR(255), count int)")
            print ("created words tables")

        if ('users',) in results:
            print ("users tables initialized")
        else:
            SQLCursor.execute("CREATE TABLE users (name VARCHAR(255), userid VARCHAR(255))")
            print ("created users tables")

    def insertNewData():
        print ("test")
