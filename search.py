import sqlite3 
class Film:
    def __init__(self):
        self.search = " "
        self.result = " "
    def get_search(self):
        return self.search
    def set_search(self, search):
        self.search = search
    
    def searchInDatabase(self):
        with sqlite3.connect("movies.db") as db:
            cursor = db.cursor()
        find_search = ("SELECT * FROM Movies WHERE Title = ?")
        #find_search = (" SELECT * FROM Movies UNION SELECT * FROM Series WHERE Title = ? ")
        #find_search = ("SELECT Title AS MOVIETITLE FROM Movies WHERE MOVIETITLE = '?' UNION SELECT TITLE AS SERIESTITLE FROM Series WHERE SERIESTITLE = '?' ")
        cursor.execute(find_search,[(self.search)])
        results = cursor.fetchall()
        if results:
            return True
        else:
            return False
    def searchTitle(self,title):
        with sqlite3.connect("movies.db") as db:
            cur = db.cursor()
        cur.execute("SELECT * FROM Movies WHERE Title = '{0}' UNION SELECT * FROM Series WHERE Title = '{0}'".format(title))
        return cur.fetchall()

    def print(self):
        results = self.searchTitle(self.get_search())
        resultCount = len(results)

        if(resultCount > 0):
            for result in results:
                print("Title: {}".format(result[1]))
                print("Description: {}".format(result[2]))
        elif(resultCount == 0):
            print("Title Not Found")

    def autoNextLine(self, string, wordsPerLine):
        string = string.split(" ")
        stringSliced = ""
        i = 0
        while i < len(string):
            if (i % wordsPerLine == 0 and i != 0):
                stringSliced += "\n"
            stringSliced += string[i] + " "
            i += 1
        return stringSliced
    def formatResult(self, title):
        results = self.searchTitle(title)
        resultCount = len(results)
        formattedOutput = ""

        if(resultCount > 0):
            for result in results:
                formattedOutput += "Title: {}".format(result[1]) + "\n"
                formattedOutput += "Description: {}".format(self.autoNextLine(result[2], 10)) + "\n"
                formattedOutput += "Rating: {}".format(result[3]) + "\n"
                formattedOutput += "Release Year: {}".format(result[4]) + "\n"
                formattedOutput += "Directors: {}".format(result[5]) + "\n"
                formattedOutput += "Cast: {}".format(self.autoNextLine(result[6], 8)) + "\n"
                formattedOutput += "Country: {}".format(result[7]) + "\n"
                formattedOutput += "Duration: {}".format(result[8]) + "\n"
        elif(resultCount == 0):
            formattedOutput += "NA"
        return formattedOutput 

    
