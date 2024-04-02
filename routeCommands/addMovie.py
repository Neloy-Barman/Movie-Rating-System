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

# Adding a new movie
@app.route("/addMovie", methods=['GET','POST'])
def AddNewMovie():

    if request.method == "POST":
        name = request.form['name']
        genre = request.form['genre']
        rating = request.form['rating']
        release_date = request.form['release_date']

        connection = psycopg2.connect(**dbParams)
        cur = connection.cursor()
        
        query = f"INSERT INTO movies(name, genre, rating, release_date) VALUES('{name}', '{genre}', '{rating}', TO_DATE('{release_date}', 'YYYY/MM/DD'));"
        cur.execute(query)

        cur.close()
        connection.commit()
        connection.close()

        print("Data added")
    return render_template("addMovie.html")


if __name__ == "__main__":
    app.run(debug=True)