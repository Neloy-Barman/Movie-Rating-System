from flask import Blueprint
from bluePrints.user.controller import login

user = Blueprint("user", __name__, template_folder="templates")

user.route("/", methods=['GET', 'POST'])(login)