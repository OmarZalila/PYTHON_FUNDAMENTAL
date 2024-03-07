from flask_app import app 
from flask import render_template,request, redirect , flash,session
from flask_app.models.recipes import Recipe
from flask_app.controllers import user_controllers



@app.route("/recipes")
def display():
    #!!!!!!!!!!!!ROUTE GUARD!!!!!!!!!!!!!!!!!!!!!
    if "user_id" not in session:
        return redirect("/")
    data ={"id" : session["user_id"]}
    current_user = user_controllers.User.get_by_id(data)
    All_recipes=Recipe.all_posted_recipe()
    return render_template("all_recipes.html",current_user=current_user,All_recipes=All_recipes)



#view route for the form 
@app.route("/recipes/new")
def display_create():

    return render_template("add_recipe.html")

#action route for create book
@app.route("/create_recipe",methods=["POST"])
def create_recipe():
    
    data={
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "date_cooked" : request.form["date_cooked"],
        "under" : request.form["under"],
        "user_id": session["user_id"]
    }
    if  not Recipe.validate_recipe(request.form):
        return redirect ("/recipes/new")
    Recipe.create(data)
    return redirect("/recipes")


@app.route("/recipes/<int:id>")
def show_one(id):
    data={
        "id" : id
    }
    one_recipe=Recipe.get_one_recipe(data)

    data ={"id" : session["user_id"]}
    current_user = user_controllers.User.get_by_id(data)
    
    return render_template("one_recipe.html", one_recipe=one_recipe,current_user=current_user)

@app.route("/recipes/edit/<int:id>")
def edit_one(id):
    data={
        "id" : id
    }
    recipe=Recipe.get_id(data)
    return render_template("edit_page.html",recipe=recipe)




@app.route("/edit/<int:id>", methods=["POST"])
def edit_recipes(id):
    if  not Recipe.validate_recipe(request.form):
        return redirect (f"/recipes/edit/{id}")
    data={
        **request.form,
        "id":id
    }
    Recipe.edit(data)
    return redirect("/recipes") 


@app.route("/delete/<int:id>")
def delete(id):
    data={
        "id" : id
    }
    Recipe.delete(data)
    return redirect("/recipes")