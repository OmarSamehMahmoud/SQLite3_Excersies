import sqlite3

con = sqlite3.connect("movies.db")

cusror = con.cursor()

cusror.execute("CREATE TABLE movie (title TEXT ,year INTEGER)")

moviess = [ ('spider',2000), ('bee',2003)]

cusror.executemany("INSERT INTO movie  VALUES (?,?)",moviess)

con.commit()

con.close()
 