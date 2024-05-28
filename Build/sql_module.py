#Placeholder

import mysql.connector


class sqlSession:
    def __init__(self):
        self.discordDB = None
        self.SQLCursor = None

    #Database Init
    def dbInit(self): 
        self.discordDB = mysql.connector.connect(host="127.0.0.1", user="root", password="admin")
        self.SQLCursor = self.discordDB.cursor()
        self.SQLCursor.execute("SHOW DATABASES")

        print ("Current SQL databases:")
        for x in self.SQLCursor:
            print(x)

        try:
            self.discordDB = mysql.connector.connect(host="127.0.0.1", user="root", password="admin", database= "discord_db")
            print ("DB link established")
        except mysql.connector.Error as err:
            self.SQLCursor.execute("CREATE DATABASE discord_db")
            self.discordDB = mysql.connector.connect(host="127.0.0.1", user="root", password="admin", database= "discord_db")
            print("Discord database not found, created new database, link established")

        self.SQLCursor = self.discordDB.cursor()

        #init default tables
        self.SQLCursor.execute("SHOW TABLES")
        results = self.SQLCursor.fetchall()
        for x in results:
            print (x)

        if ('words',) in results:
            print ("words tables initialized")
        else:
            self.SQLCursor.execute("CREATE TABLE words (id INT AUTO_INCREMENT PRIMARY KEY, word VARCHAR(255), userid VARCHAR(255), count int)")
            print ("created words tables")

        if ('users',) in results:
            print ("users tables initialized")
        else:
            self.SQLCursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), userid VARCHAR(255))")
            print ("created users tables")

        if ('overall_words',) in results:
            print ("overall_words tables initialized")
        else:
            self.SQLCursor.execute("CREATE TABLE overall_words (id INT AUTO_INCREMENT PRIMARY KEY, word VARCHAR(255), count int)")
            print ("created overall_words tables")

    def insertUser(self, ctx):
        self.SQLCursor.execute("SELECT userid, COUNT(*) FROM users WHERE userid = %s GROUP BY userid", (ctx.author.id,)) #select userid column, from table "users", where userid == given name
        self.SQLCursor.fetchall()

        row_count = self.SQLCursor.rowcount
        #print (row_count)

        if (row_count == 0):
            self.SQLCursor.execute("INSERT INTO users (name, userid) VALUES (%s, %s)", [(ctx.author.name), (ctx.author.id)])
            self.discordDB.commit()
            print ("inserted " + ctx.author.name)

    def insertWordUsage(self, ctx):
        strmessage = ctx.content
        if (strmessage.find("$") != -1): #likely a command if $ is used
            print ("command ignored")
            return
        strmessage = strmessage.lower()
        wordList = strmessage.split() 

        #insertion to user words
        for x in wordList:
            if (x.find("@") != -1): #likely a ping if used
                continue

            self.SQLCursor.execute("SELECT word, userid, count, COUNT(*) FROM words WHERE word = %s and userid = %s GROUP BY word, userid, count", (x ,ctx.author.id)) #select userid column, from table "users", where userid == given name
            row_data = self.SQLCursor.fetchall() #gets the row where the given word was already said (if any), data is formatted as a list of tuples

            row_count = self.SQLCursor.rowcount
            if (row_count == 0):
                self.SQLCursor.execute("INSERT INTO words (word, userid, count) VALUES (%s, %s, %s)", [x, (ctx.author.id), 1])
                self.discordDB.commit()
                print ("inserted overall " + x)
            else:
                #print(row_data[0][2])
                
                data = [row_data[0][2] + 1, ctx.author.id, x]
                self.SQLCursor.execute("UPDATE words SET count = %s WHERE userid = %s and word = %s", data)
                self.discordDB.commit()
                print ("updated " + x)
        
        #insertion to overall words
        for x in wordList:
            if (x.find("@") != -1): #likely a command if $ is used
                continue

            self.SQLCursor.execute("SELECT word, count, COUNT(*) FROM overall_words WHERE word = %s GROUP BY word, count", [(x),]) #select userid column, from table "users", where userid == given name
            row_data = self.SQLCursor.fetchall() #gets the row where the given word was already said (if any), data is formatted as a list of tuples

            row_count = self.SQLCursor.rowcount
            if (row_count == 0):
                self.SQLCursor.execute("INSERT INTO overall_words (word, count) VALUES (%s, %s)", [x, 1])
                self.discordDB.commit()
            else:
                data = [row_data[0][1] + 1, x]
                self.SQLCursor.execute("UPDATE overall_words SET count = %s WHERE word = %s", data)
                self.discordDB.commit()

    def getWordUsage(self):
        self.SQLCursor.execute("SELECT word, count, COUNT(*) FROM overall_words GROUP BY word, count ORDER BY count DESC LIMIT 20") 
        row_data = self.SQLCursor.fetchall()
        print (row_data)
        return row_data #must parse the returned list of tuples


