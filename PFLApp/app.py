
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    return render_template('index.html')

# Add login, dashboard, pick submission routes here

if __name__ == '__main__':
    app.run(debug=True)
