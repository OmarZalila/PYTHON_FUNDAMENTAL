from flask import Flask , render_template , session , redirect , request
app = Flask(__name__)   
app.secret_key = '25sd25xjdnnskaldn4555'

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/display")
def display_info():
    return render_template("form.html")

@app.route("/submit", methods=['POST'])
def display():
    session["info"]=request.form

    return redirect("/display")

@app.route("/go_back")
def back():
    return redirect("/")

if __name__=="__main__":  
    app.run(debug=True )  