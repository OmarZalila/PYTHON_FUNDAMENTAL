from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


#* view route 
@app.route("/add_ninja")
def add_ninja():
    all_dojos=Dojo.display()
    return render_template("add.html", all_dojos=all_dojos)

@app.route("/add_one" , methods=["POST"])
def add_one():
    data={
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo']
    }
    Ninja.save(data)
    return redirect("/dojo")

