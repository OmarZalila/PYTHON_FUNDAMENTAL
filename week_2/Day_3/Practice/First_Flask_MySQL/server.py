from flask import Flask, render_template,redirect,request
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/home")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users)

@app.route("/users/create")
def display_form():

    return render_template("create.html")

@app.route("/users/new" , methods=["POST"])
def create_user():
    User.save(request.form)
    print(request.form)
    return redirect("/home")

            
if __name__ == "__main__":
    app.run(debug=True)

