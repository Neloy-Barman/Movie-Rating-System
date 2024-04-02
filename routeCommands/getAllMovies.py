import psycopg2
from flask import Flask
from flask import render_template

app = Flask(__name__)

dbParams = {
    "host": "localhost",
    "database": "movieRatingSystem",
    "user": "postgres",
    "password": "1234", 
}

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

if __name__ == "__main__":
    app.run(debug=True)