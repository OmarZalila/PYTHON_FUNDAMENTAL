from flask import Flask  
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def Dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
    return name * num

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No response. Try again.', 404

if __name__=="__main__":     
    app.run(debug=True)    





