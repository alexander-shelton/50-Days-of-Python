#!/usr/bin/env python3
#
# Day 49: Create a Database

import sqlite3

# Create Database
print("Create Database")
conn = sqlite3.connect('my_movies.db')
curr = conn.cursor()
try:
    curr.execute('CREATE TABLE movies(year,title,genre)')
except sqlite3.OperationalError:
    print("Table already exists")
movies = [
    (2009, 'Brothers', 'Drama'),
    (2002, 'Spider-Man', 'Sci-fi'),
    (2009, 'WatchMen', 'Drama'),
    (2010, 'Inception', 'Sci-fi'),
    (2009, 'Avatar', 'Fantasy'),
]
curr.executemany('''INSERT INTO movies VALUES(?, ?, ?)''', movies)
conn.commit()
conn.close()


# 1) Query to see movies in the database
print("\na) Query to see movies in the database")
conn = sqlite3.connect('my_movies.db')
curr = conn.cursor()
for movie in curr.execute('SELECT * FROM movies;'):
    print(movie)


# 2) Query movie by title.
print("\nb) Query movie by title.")
for movie in curr.execute('SELECT * FROM movies WHERE title="Brothers";'):
    print(movie)


# 3) Query movies by year.
print("\nc) Query movies by year.")
for movie in curr.execute('SELECT * FROM movies where year=2009;'):
    print(movie)


# 4) Get movies with genre of 'Drama' or 'Fantasy'.
print("\nd) Get movies with genre of 'Drama' or 'Fantasy'.")
for movie in curr.execute('SELECT * FROM movies WHERE genre="Drama" or genre="Fantasy";'):
    print(movie)


# 5) Delete the table.
print("\ne) Delete the table.")
curr.execute('DELETE FROM movies;')
conn.commit()
curr.close()