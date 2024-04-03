import sys
from flask import Flask
from bluePrints.user.user import user
from bluePrints.movies.movies  import movies
from bluePrints.ratings.ratings import ratings

# To avoid generating pycache 
sys.dont_write_bytecode = True

app = Flask(__name__)

app.secret_key = 'Movie_Rating_System'


app.register_blueprint(user)

app.register_blueprint(movies)

app.register_blueprint(ratings)

if __name__ == "__main__":
    app.run(debug=True)