from flask import Flask, render_template
import os
from dotenv import load_dotenv
from datetime import datetime
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    
    day_of_week = datetime.today().strftime('%A, %B %d, %Y')
    
    return render_template('index.html', day_of_week=day_of_week)

if __name__ == '__main__':
    app.run(debug=True)
