from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import render_template
from flask_jwt_extended import create_access_token

from bluePrints.user.model import fetchUser

DATABASE_URI = "postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db"

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email and password:
            userData = fetchUser(email=email, password=password)
            if userData:
                access_token  = create_access_token(identity = userData[0])
                print(f"This is access token: {access_token}")
                session['userId'] = userData[0]
                session['authorizationToken'] = access_token
                return redirect("/movies")
            else:
                return {"message": "Invalid Credentials!!"}
        
    return render_template('login.html')