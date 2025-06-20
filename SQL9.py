import sqlite3

con = sqlite3.connect("movies.db")

cursor = con.cursor()

cursor.execute("CREATE TABLE movies(Title TEXT, Year INTEGER)")

moviess = [('spider',2000), ('bee',2003) ,  ('beeS',2001)]

cursor.executemany("INSERT INTO movies  VALUES (?,?)",moviess)

data = cursor.execute ("SELECT Title,Year FROM movies WHERE Year BETWEEN 2000 AND 2003")


for row in data:
    print(row[0])
    
con.commit()

con.close()
    