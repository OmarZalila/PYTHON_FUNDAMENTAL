from flask_app import app 
from flask import render_template,request, redirect , flash,session
from flask_bcrypt import Bcrypt
from flask_app.models.users import User

bcrypt = Bcrypt(app)

#view route
@app.route("/")
def login():
    return render_template("login.html")

#action route
#======Registration=========
@app.route("/register" , methods=["POST"])
def process_register():

    # validate the form here ...
    if not User.validate_user(request.form):
        return redirect ("/")
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print("=========>",pw_hash)
    data={
        **request.form,
        "password" : pw_hash
    }

    user_id=User.create(data)
    session["user_id"]=user_id

    return redirect("/recipes")

#action route
#======Login=========
@app.route("/login" , methods=["POST"])
def process_login():

    if not User.validate_login_user(request.form):
        return redirect ("/")
    # if the username provided exist to database
    data={
        "email" : request.form["email"]
    }
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("*Invalid Email/Password", "email_login")
        return redirect("/")
    # validate the form here ...
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("*Invalid Email/Password", "password_login")
        return redirect("/")
    session["user_id"]=user_in_db.id
    return redirect("/recipes")

# @app.route("/home")
# def display():
#     #!!!!!!!!!!!!ROUTE GUARD!!!!!!!!!!!!!!!!!!!!!
#     if "user_id" not in session:
#         return redirect("/")
#     data ={"id" : session["user_id"]}
#     current_user = User.get_by_id(data)
#     return render_template("dashbord.html",current_user=current_user)

#LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")