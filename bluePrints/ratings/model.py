import psycopg2

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

def insertRatings(userId:int , movieId: int, rating: float) -> bool:

    connection = psycopg2.connect(DATABASE_URI)
    cur = connection.cursor()

    query = f"INSERT INTO ratings(user_id, movie_id, rating) VALUES({userId}, {movieId}, {rating});"

    cur.execute(query)
    connection.commit()

    cur.close()
    connection.close()

    return True

def averageRating(movieId: int):

    connection = psycopg2.connect(DATABASE_URI)
    cur = connection.cursor()

    query = f"SELECT AVG(rating) FROM ratings WHERE movie_id={movieId};"
    cur.execute(query)

    avgRatings = cur.fetchone()

    cur.close()
    connection.close()

    return avgRatings[0]
