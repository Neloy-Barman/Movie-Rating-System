from flask import request
from flask import session
from flask import render_template

from bluePrints.movies.model import fetchMovie
from bluePrints.movies.model import fetchMovies
from bluePrints.movies.model import insertMovie
from bluePrints.ratings.controller import addRatings
from bluePrints.ratings.controller import avgRatings

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

# Fetch all the movies from the database
def allMovies():
    if "authorizationToken" in session:
        movies = fetchMovies()
        if movies:
            return render_template("allMovies.html", movies = movies)
    else:
        return render_template("notAvailable.html")
    
# Fetch a specific movie details
def movieDetails(movieId: int):
    if "authorizationToken" in session:
        movie = fetchMovie(movieId=movieId)
        average = avgRatings(movieId=movieId)
        
        if average == 0 or not average:
            average = "Not Rated yet!!"
        else:
            average = round(average, 2) 

        if not movie or not average:
            return {"message": "An unexpected error occured!!"}
        
        print(f"This is average: {average}")

        if request.method == 'POST':
            rating = request.form['rating']
            return addRatings(movieId=movieId, rating=float(rating))
        
        return render_template('movieDetails.html', movie = movie, average = average)
    else:
        return render_template("notAvailable.html")


# Adding a new movie to the database
def addMovie():
    if "authorizationToken" in session:
        if request.method == "POST":
            name = request.form['name']
            genre = request.form['genre']
            rating = request.form['rating']
            release_date = request.form['release_date']

        add = insertMovie(name=name, genre=genre, rating=rating, release_date=release_date)

        if add:
            return {"message": "Movie added successfully!!"}

        return render_template("addMovie.html")
    else:
        return render_template("notAvailable.html")