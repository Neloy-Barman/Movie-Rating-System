import psycopg2
from flask import request
from flask import session
from flask import redirect
from flask import render_template

def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        if email and password:
            # connection = psycopg2.connect(**dbParams)
            connection = psycopg2.connect("postgres://mrs_db_user:1zfGVbsqEWLfl4tTKn3ZwXmoWqtYhNUj@dpg-co62pt6v3ddc7399i9h0-a.oregon-postgres.render.com/mrs_db")
            cur = connection.cursor()

            query = f"SELECT * FROM users WHERE email='{email}' and password='{password}';"
            
            cur.execute(query)
            userData = cur.fetchone()
            
            if userData:
                # print("Redirect")
                session['userId'] = userData[0]
                print(f"This is user Id: {session['userId']}")
                return redirect('movies')
        else:
            print("Empty value")

    return render_template('login.html')

