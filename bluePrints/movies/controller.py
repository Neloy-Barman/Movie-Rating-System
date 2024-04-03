import psycopg2
from flask import request
from flask import render_template
from bluePrints.ratings.controller import addRatings

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

# Fetch all the movies from the database
def allMovies():
    connection = psycopg2.connect(DATABASE_URI)
    query = "SELECT * FROM movies;"
    cur = connection.cursor()
    cur.execute(query)
    movies = cur.fetchall()

    cur.close()
    connection.close()

    return render_template("allMovies.html", movies = movies)

# Fetch a specific movie details
def movieDetails(movieId: int):
    connection = psycopg2.connect(DATABASE_URI)
    cur = connection.cursor()

    movieQuery = f"SELECT * FROM movies WHERE id={movieId};"
    cur.execute(movieQuery)
    movie = cur.fetchone()

    ratingQuery = f"SELECT AVG(rating) FROM ratings WHERE movie_id={movieId};"
    cur.execute(ratingQuery)
    avgRatings = cur.fetchone()

    if not movie:
        return {"Error": "Movie not found!!!!"}
    
    if request.method == 'POST':
        rating = request.form['rating']
        return addRatings(movieId=movieId, rating=float(rating))
    
    return render_template('movieDetails.html', movie = movie, avgRatings = round(avgRatings[0], 2))


# Adding a new movie to the database
def addMovie():
    if request.method == "POST":
        name = request.form['name']
        genre = request.form['genre']
        rating = request.form['rating']
        release_date = request.form['release_date']

        connection = psycopg2.connect(DATABASE_URI)
        cur = connection.cursor()
        
        query = f"INSERT INTO movies(name, genre, rating, release_date) VALUES('{name}', '{genre}', '{rating}', TO_DATE('{release_date}', 'YYYY/MM/DD'));"
        cur.execute(query)

        cur.close()
        connection.commit()
        connection.close()

        print("Data added")
    return render_template("addMovie.html")