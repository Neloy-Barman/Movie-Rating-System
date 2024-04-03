import psycopg2
from flask import session

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

def addRatings(movieId: int, rating: float):

    connection = psycopg2.connect(DATABASE_URI)
    cur = connection.cursor()

    query = f"INSERT INTO ratings(user_id, movie_id, rating) VALUES({session['userId']}, {movieId}, {rating});"

    cur.execute(query)
    cur.close()

    connection.commit()
    connection.close()

    return {"message": "Rated successfully!!"}