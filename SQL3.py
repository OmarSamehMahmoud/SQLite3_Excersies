import sqlite3

con = sqlite3.connect("movies.db")

cusror = con.cursor()

cusror.execute("CREATE TABLE movie (title TEXT ,year INTEGER)")

cusror.execute("INSERT INTO movie(title,year) VALUES ('Spider',2000)")

con.commit()

con.close()
 