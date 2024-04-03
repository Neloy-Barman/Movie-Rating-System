import psycopg2
from psycopg2 import OperationalError, Error

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

def fetchUser(email: str, password: str):
    connection = psycopg2.connect(DATABASE_URI)
    cur = connection.cursor()

    query = f"SELECT id FROM users WHERE email='{email}' and password='{password}';"

    cur.execute(query)
    userData = cur.fetchone()
    
    cur.close()
    connection.close()

    return userData