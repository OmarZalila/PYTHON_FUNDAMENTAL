from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route("/home")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users)

@app.route("/users/create")
def display_form():

    return render_template("create.html")

@app.route("/users/new" , methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect("/home")

@app.route("/users/delete/<int:id>")
def delete(id):
    data={
        'id':id
    }
    User.delete_user(data)
    return redirect('/home')

@app.route("/users/update/<int:id>")
def show_update(id):

    data={
        'id':id
    }
    one_user=User.get_one_by_id(data)
    return render_template("edit.html", one_user=one_user)
@app.route("/users/show/<int:id>")
def show_user(id):

    data={
        'id':id
    }
    one_user=User.get_one_by_id(data)
    return render_template("show.html", one_user=one_user)

@app.route("/users/edit/<int:id>" , methods=["POST"])
def user_update(id):
    user_dict={
        'id' : id ,
        **request.form
    }
    User.update(user_dict)
    return redirect("/home")