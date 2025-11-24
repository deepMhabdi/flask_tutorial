from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from bson import ObjectId

app = Flask(__name__)

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

uri = "mongodb+srv://dmmhabdi2701_db_user:1234@cluster0.4v0fh4k.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

# Ping database
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(e)

# FIX: define DB + collection
db = client["flask_database"]     
collection = db["form_data"]      

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)
    return jsonify({"message": "Data sent successfully"})

@app.route('/view')
def view():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify({"data": data})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
