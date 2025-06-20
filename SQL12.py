import sqlite3

con = sqlite3.connect("movies.db")

cursor = con.cursor()

cursor.execute("CREATE TABLE movies(Title TEXT, Year INTEGER)")

moviess = [('spider',2000), ('bee',2003) ,  ('beeS',2001)]

cursor.executemany("INSERT INTO movies  VALUES (?,?)",moviess)

cursor.execute("UPDATE movies SET Title = 'hi' WHERE rowid = 2")

cursor.execute ("DROP movies")
    
con.commit()

con.close()
    