import sqlite3

con = sqlite3.connect("movies.db")
cursor  = con.cursor()
cursor.execute("CREATE TABLE movie ('Name TEXT, Year INTERGER')")
con.commit()
con.close()