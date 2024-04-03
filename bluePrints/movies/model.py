import psycopg2

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

def fetchMovies():
    connection = psycopg2.connect(DATABASE_URI)
    cur = connection.cursor()
    
    query = "SELECT * FROM movies;"
    cur.execute(query)

    movies = cur.fetchall()

    cur.close()
    connection.close()

    if movies:
        return movies
    return None

def fetchMovie(movieId: int):
    connection = psycopg2.connect(DATABASE_URI)
    cur = connection.cursor()

    movieQuery = f"SELECT * FROM movies WHERE id={movieId};"
    cur.execute(movieQuery)
    movie = cur.fetchone()

    cur.close()
    connection.close()

    if movie:
        return movie


def insertMovie(name: str, genre: str, rating: str, release_date: str) -> bool:

    connection = psycopg2.connect(DATABASE_URI)
    cur = connection.cursor()

    query = f"INSERT INTO movies(name, genre, rating, release_date) VALUES('{name}', '{genre}', '{rating}', TO_DATE('{release_date}', 'YYYY/MM/DD'));"
    cur.execute(query)
    connection.commit()

    cur.close()
    connection.close()

    return True




