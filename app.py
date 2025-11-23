from flask import Flask, request, render_template
import os
from dotenv import load_dotenv
from datetime import datetime
from pymongo.mongo_client import MongoClient

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

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A, %B %d, %Y')
    return render_template('index.html', day_of_week=day_of_week)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return "Data submitted successfully"

@app.route('/view')
def view():
    
    data = collection.find()
    
    data = list(data)
    
    for item in data: 
    
        print(item)
        
        del item['_id']
        
    data = {
        'data': data
    }
    
    return data

if __name__ == '__main__':
    app.run(debug=True)
