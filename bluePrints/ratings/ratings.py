from flask import Blueprint
from bluePrints.ratings.controller import addRatings

ratings = Blueprint("ratings", __name__, template_folder="templates")

ratings.route("/addRatings", methods=['GET', 'POST'])(addRatings)

