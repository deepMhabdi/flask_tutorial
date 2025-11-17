from flask import Flask, request, render_template
app = Flask(__name__)

from datetime import datetime
datetime.today().strftime('%A')
'Monday'

@app.route('/')
def home():
    
    day_of_week = datetime.today().strftime('%A') + datetime.today().strftime(', %B %d, %Y')
    
    current_time = datetime.today().strftime(' - %I:%M %p')
    
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)



if __name__ == '__main__':

    app.run(debug=True)
    