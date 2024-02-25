from flask import Flask , render_template
app = Flask(__name__)   
@app.route('/play')
def index():
    return render_template("index.html")

@app.route('/play/<int:x>')
def repeat(x):
    return render_template("index.html" , time=x)
if __name__=="__main__":  
    app.run(debug=True)    

