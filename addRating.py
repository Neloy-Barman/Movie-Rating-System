import psycopg2
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

dbParams = {
    "host": "localhost",
    "database": "movieRatingSystem",
    "user": "postgres",
    "password": "1234", 
}

# Fetching a specific movie
@app.route("/movies/<int:movieId>", methods=['GET', 'POST'])
def specificMovie(movieId: int):

    connection = psycopg2.connect(**dbParams)
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

        connection = psycopg2.connect(**dbParams)
        cur = connection.cursor()

        query = f"INSERT INTO ratings(user_id, movie_id, rating) VALUES(1, {movieId}, {float(rating)});"

        cur.execute(query)
        cur.close()

        connection.commit()
        connection.close()

        print("Ratings added")

    return render_template('movieDetails.html', movie = movie, avgRatings = round(avgRatings[0], 2))

if __name__ == "__main__":
    app.run(debug=True)