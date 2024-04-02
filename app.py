from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    # return render_template('login.html')
    # return render_template('addMovie.html')
    # return render_template('movieDetails.html')
    return render_template('allMovies.html')

if __name__ == "__main__":
    app.run(debug=True)