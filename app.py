import sys 
# To avoid generating pycache 
sys.dont_write_bytecode = True

import psycopg2
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from bluePrints.user.user import user

app = Flask(__name__)

app.secret_key = 'Movie_Rating_System'


app.register_blueprint(user)

# dbParams = {
#     "host": "localhost",
#     "database": "movieRatingSystem",
#     "user": "postgres",
#     "password": "1234", 
# }

dbParams = {
    "host": "localhost",
    "database": "movieRatingSystem",
    "user": "postgres",
    "password": "1234", 
}


# @app.route("/", methods=['GET','POST'])
# def loginPage():
#     if request.method == 'POST':

#         email = request.form.get('email')
#         password = request.form.get('password')

#         if email and password:
#             # connection = psycopg2.connect(**dbParams)
#             connection = psycopg2.connect("postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db")
#             cur = connection.cursor()

#             query = f"SELECT * FROM users WHERE email='{email}' and password='{password}';"
            
#             cur.execute(query)
#             userData = cur.fetchone()
            
#             if userData:
#                 # print("Redirect")
#                 session['userId'] = userData[0]
#                 print(f"This is user Id: {session['userId']}")
#                 return redirect('movies')
#         else:
#             print("Empty value")

#     return render_template('login.html')


# Fetching all the movies from database
@app.route("/movies", methods=['GET'])
def getAllMovies():

    connection = psycopg2.connect(**dbParams)

    query = "SELECT * FROM movies;"
    cur = connection.cursor()
    cur.execute(query)
    movies = cur.fetchall()

    cur.close()
    connection.close()

    return render_template("allMovies.html", movies = movies)


# Fetching a specific movie
@app.route("/movies/<int:movieId>", methods=['GET'])
def specificMovie(movieId: int):

    connection = psycopg2.connect(**dbParams)
    cur = connection.cursor()

    movieQuery = f"SELECT * FROM movies WHERE id={movieId};"
    cur.execute(movieQuery)
    movie = cur.fetchone()

    ratingQuery = f"SELECT AVG(rating) FROM ratings WHERE movie_id={movieId};"
    cur.execute(ratingQuery)
    avgRatings = cur.fetchone()

    print(f"This is user_id: {session['userId']}")

    if not movie:
        return {"Error": "Movie not found!!!!"}
    
    return render_template('movieDetails.html', movie = movie, avgRatings = round(avgRatings[0], 2))



if __name__ == "__main__":
    app.run(debug=True)