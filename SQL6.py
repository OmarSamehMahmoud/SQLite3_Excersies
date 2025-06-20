import sqlite3

con = sqlite3.connect("movies.db")

cursor = con.cursor()

cursor.execute("CREATE TABLE movies(Title TEXT, Year INTEGER)")

cursor.execute("INSERT INTO movies(Title,Year) VALUES ('Spider',2000)")

cursor.execute ("SELECT * FROM movies")

print(cursor.fetchone())

print(cursor.fetchall())

print(cursor.fetchmany(2))
    
    
con.commit()

con.close()
    