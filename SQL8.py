import sqlite3

con = sqlite3.connect("movies.db")

cursor = con.cursor()

cursor.execute("CREATE TABLE movies(Title TEXT, Year INTEGER)")

cursor.execute("INSERT INTO movies(Title,Year) VALUES ('Spider',2000)")

data = cursor.execute ("SELECT Title,Year FROM movies ORDER BY Year DESC LIMIT 1")

for row in data:
    print(row[0])
    
    
con.commit()

con.close()
    