import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template(
        'reviews.html', reviews=mongo.db.reviews.find())


@app.route('/add_review')
def add_review():
    return render_template(
        'addreview.html', reviews=mongo.db.reviews.find())


@app.route('/insert_review', methods=['POST'])
def insert_review():



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
