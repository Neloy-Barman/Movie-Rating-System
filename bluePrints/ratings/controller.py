from flask import session
from bluePrints.ratings.model import insertRatings
from bluePrints.ratings.model import averageRating

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

def addRatings(movieId: int, rating: float):
    rate = insertRatings(userId=session['userId'], movieId=movieId, rating=rating)
    if rate:
        return {"message": "Rated successfully!!"}
    
def avgRatings(movieId: int):
    ratings = averageRating(movieId=movieId)
    if ratings:
        return ratings
    