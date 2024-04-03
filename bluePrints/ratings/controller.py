from flask import session
from flask import render_template
from bluePrints.ratings.model import insertRatings
from bluePrints.ratings.model import averageRating

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

def addRatings(movieId: int, rating: float):
    if "authorizationToken" in session:
        rate = insertRatings(userId=session['userId'], movieId=movieId, rating=rating)
        if rate:
            return {"message": "Rated successfully!!"}
    else:
        return render_template("notAvailable.html")
    
def avgRatings(movieId: int):
    if "authorizationToken" in session:
        ratings = averageRating(movieId=movieId)
        if ratings:
            return ratings
    else:
        return render_template("notAvailable.html")