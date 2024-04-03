from flask import Blueprint
from bluePrints.movies.controller import allMovies
from bluePrints.movies.controller import movieDetails
from bluePrints.movies.controller import addMovie

movies = Blueprint("movies", __name__, template_folder="templates")

movies.route("/movies", methods=['GET'])(allMovies)
movies.route("/movies/<int:movieId>", methods=['GET', 'POST'])(movieDetails)
movies.route("/addMovie", methods=['GET', 'POST'])(addMovie)