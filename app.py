import sys
# To avoid generating pycache 
sys.dont_write_bytecode = True

from flask import Flask
from flask_jwt_extended import JWTManager

from bluePrints.user.user import user
from bluePrints.movies.movies  import movies
from bluePrints.ratings.ratings import ratings

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "446B1D2D461AE3B413D9B9277961C"
app.secret_key = 'Movie_Rating_System'

jwt = JWTManager(app)

app.register_blueprint(user)

app.register_blueprint(movies)

app.register_blueprint(ratings)

if __name__ == "__main__":
    app.run(debug=True)