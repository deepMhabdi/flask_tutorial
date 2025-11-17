from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/api')
def name():
    
    name = request.values.get('name')
    age = request.values.get('age')
    
    age = int(age)
    name = str(name)
    
    if age > 18:
        return "Welcome to the site,  " + name + "!"
    
    else: 
        return "Sorry, " + name + " you are too young to use this site"

if __name__ == '__main__':

    app.run(debug=True)
    