from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

users = [
    { 
        "id":1, 
        "name": "John Doe", 
        "phone":"11111111111", 
        "password":"pass1", 
        "email":"john_doe@gmail.com" 
    }, 
    { 
        "id":2, 
        "name": "Jane Doe", 
        "phone":"22222222222", 
        "password":"pass2", 
        "email":"jane_doe@gmail.com" 
    }, 
    { 
        "id":3, 
        "name": "Mark Doe", 
        "phone":"3333333333", 
        "password":"pass3", 
        "email":"mark_doe@gmail.com" 
    }, 
    { 
        "id":4, 
        "name": "Macy Doe", 
        "phone":"4444444444", 
        "password":"pass4", 
        "email":"macy_doe@gmail.com" 
    } 
] 


@app.route("/login", methods=["GET"])
def login(email: str, password: str):
    for user in users:
        if user["email"] == email and user["password"] == password:
            return getAllMovies() 
    return {"Error": "Invalid credentials"}



# @app.route("/users", methods=["POST"])
# def 

movies = [
    {
        "id": 1,
        "name": "Home Alone",
        "genre": "Comedy",
        "rating": "PG",
        "release_date": "01-04-1996"
    },
    {
        "id": 2,
        "name": "The Godfather",
        "genre": "Crime",
        "rating": "R",
        "release_date": "01-04-1972"
    },
    {
        "id": 3,
        "name": "Avengers: Endgame",
        "genre": "Action",
        "rating": "PG",
        "release_date": "01-04-2019"
    },
]


# Fetching all the movies from database
@app.route("/movies", methods=['GET'])
def getAllMovies():
    allMovies = movies
    return render_template("allMovies.html", movies = allMovies)

# Fetching a specific movie
@app.route("/movies/<int:movieId>", methods=['GET'])
def specificMovie(movieId: int):
    for movie in movies:
        if movie['id'] == movieId:
            avgRatings = getRatings(movieId=movieId)
            return render_template('movieDetails.html', movie = movie, avgRatings = round(avgRatings[0], 2))
    return {'Error': 'Movie Not Found!!!'}

# Adding a new movie to the database
@app.route("/movies", methods=['POST'])
def addMovie():
    movie = {
        'id': len(movies)+1,
        'name': request.json['name'],
        'genre': request.json['genre'],
        'rating': request.json['rating'],
        'release_date': request.json['release_date']
    }
    movies.append(movie)
    return movie



ratings = [ 
  { 
    "id":1, 
    "user_id":1, 
    "movie_id":1, 
    "rating:": 5.0 
  }, 
  { 
    "id":2, 
    "user_id":1, 
    "movie_id":2, 
    "rating:": 4.0 
  }, 
  { 
    "id":3, 
    "user_id":1, 
    "movie_id":3, 
    "rating:": 3.3 
  }, 
  { 
    "id":4, 
    "user_id":2, 
    "movie_id":1, 
    "rating:": 5.0 
  }, 
  { 
    "id":5, 
    "user_id":2, 
    "movie_id":3, 
    "rating:": 4.5 
  }, 
  { 
    "id":6, 
    "user_id":3, 
    "movie_id":1, 
    "rating:": 1.6 
  }, 
  { 
    "id":7, 
    "user_id":3, 
    "movie_id":2, 
    "rating:": 0.0 
  }, 
  { 
    "id":8, 
    "user_id":3, 
    "movie_id":3, 
    "rating:": 3.4 
  }, 
  { 
    "id":9, 
    "user_id":4, 
    "movie_id":2, 
    "rating:": 4.5 
  } 
]

# Give a new rating to a movie
@app.route("/ratings", methods=['POST'])
def placeRatings():
    rating = {
        "id": request.json['id'],
        "user_id": request.json['user_id'],
        "movie_id": request.json['movie_id'],
        "rating:": request.json['rating:'],
    }
    ratings.append(rating)
    return rating

# Get average ratings for a movie
@app.route("/ratings/<int:movieId>", methods=['GET'])
def getRatings(movieId: int):
    sum, counter = 0.0, 0
    for r in ratings:
        if r['movie_id'] == movieId:
            sum += r['rating:']
            counter += 1
    if sum == 0:
        return {"average_ratings": "Not rated yet"}
    avgSum = sum / counter
    return {"average_ratings": round(avgSum, 2)} 



@app.route("/", methods = ['GET', 'POST'])
def index():
    # return render_template('login.html')
    return render_template('addMovie.html')
    # return render_template('movieDetails.html')
    # return render_template('allMovies.html')

if __name__ == "__main__":
    app.run(debug=True)