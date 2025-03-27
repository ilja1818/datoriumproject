from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import json
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/page')
def page():
    return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
    db.create_all()