from flask_app import app
from flask import render_template, redirect, request , session
from flask_app.models.dojo import Dojo

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def save():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data ={
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comment' : request.form['comment']
    }
    save_data=Dojo.save(data)
    return redirect(f"/display/{save_data}")

@app.route("/display/<int:id>")
def display_info(id):
    data={
        'id':id
    }
    new=Dojo.display(data)
    return render_template("form.html", new=new)

@app.route("/go_back")
def back():
    return redirect("/")



