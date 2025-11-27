from flask import Flask, request, redirect, render_template
from pymongo import MongoClient

app = Flask(__name__)

uri = "mongodb+srv://dmmhabdi2701_db_user:1234@cluster0.4v0fh4k.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

db = client["flask_database"]
collection = db["form_data"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")

        data = {"name": name, "email": email}
        collection.insert_one(data)

        return redirect("/success")
    except Exception as e:
        return render_template("index.html", error=str(e))

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)
