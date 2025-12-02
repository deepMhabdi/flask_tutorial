from flask import Flask, request, redirect, render_template_string
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://dmmhabdi2701_db_user:3456@cluster0.4v0fh4k.mongodb.net/?appName=Cluster0")
db = client["mydatabase"]
collection = db["formdata"]

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")

        data = {"name": name, "email": email}
        collection.insert_one(data)

        return redirect("/success")  
    except Exception as e:
        return f"<h3 style='color:red;'>Error: {str(e)}</h3>"

@app.route('/success')
def success():
    return "<h1>Data submitted successfully</h1>"

if __name__ == '__main__':
    app.run(debug=True)
