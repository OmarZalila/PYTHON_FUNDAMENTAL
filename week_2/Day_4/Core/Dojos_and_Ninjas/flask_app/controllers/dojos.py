from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route("/dojo")
def display_Dojo():
    all_dojos=Dojo.display()
    return render_template("index.html", all_dojos=all_dojos)

@app.route("/add_new", methods=["POST"])
def add_new():
    
    data={
        'name': request.form['name']
    }
    Dojo.add(data)
    return redirect("/dojo")

@app.route("/dojos/<int:id>")
def show_dojos(id):
    data={
        "id" : id
    }
    all_ninjas=Dojo.show(data)
    return render_template("show.html", all_ninjas=all_ninjas)