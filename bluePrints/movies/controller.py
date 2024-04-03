import psycopg2
from flask import render_template

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

def allMovies():
    connection = psycopg2.connect(DATABASE_URI)
    query = "SELECT * FROM movies;"
    cur = connection.cursor()
    cur.execute(query)
    movies = cur.fetchall()

    cur.close()
    connection.close()

    return render_template("allMovies.html", movies = movies)



