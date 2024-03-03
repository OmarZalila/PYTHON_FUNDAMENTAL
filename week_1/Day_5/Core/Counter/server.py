from flask import Flask , render_template , session , redirect , request
app = Flask(__name__)   
app.secret_key = '25sd25xjdnnskaldn45'

@app.route("/")
def index():
    if 'fromDestroy' in session:
        session["count"]=1
        session.pop('fromDestroy')
    elif 'countbytwo' in session:
        session['count']+=2
        session.pop('countbytwo')
    elif 'increase_number' in session:
        session["count"] += session["increase_number"]
        session.pop('increase_number')
    elif 'count' and 'visit' in session:
        session['count']+=1
        session['visit']+=1
    else:
        session['count']=1
        session['visit']=1
    return render_template("index.html")


@app.route("/count")
def increase():
    session["count"]+=1
    return render_template ("index.html")

@app.route("/destroy_session")
def destroy():
    session["fromDestroy"]='a'
    return redirect("/")

@app.route("/increase_by_2")
def increase_by_two():
    session["countbytwo"]='a'
    return redirect ("/")

@app.route("/Add_Number", methods=['POST'])
def add_number():
    session["increase_number"]=int(request.form['numbeeer'])
    return redirect ("/")



if __name__=="__main__":  
    app.run(debug=True )    