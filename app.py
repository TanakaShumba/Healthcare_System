from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Home route
@app.route('/')
def index():
    return render_template('index.html')  # Make sure you create 'index.html' in templates folder

# Login route (example)
@app.route('/login')
def login():
    return render_template('login.html')  # Make sure to create 'login.html'

# Appointment route (example)
@app.route('/appointments')
def appointments():
    return render_template('appointments.html')  # Make sure to create 'appointments.html'

if __name__ == '__main__':
    app.run(debug=True)
