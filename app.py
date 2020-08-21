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


# @app.route('/')
# @app.route('/get_reviews')
# def get_reviews():
#     return render_template(
#         'reviews.html', reviews=mongo.db.reviews.find())


@app.route('/get_review/<review_id>')
def get_review(review_id):
    the_review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('getreview.html', review=the_review)


@app.route('/add_review')
def add_review():
    return render_template(
        'addreview.html', reviews=mongo.db.reviews.find())


@app.route('/insert_review', methods=['POST'])
def insert_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('browse_reviews'))


@app.route('/browse_reviews')
def browse_reviews():
    return render_template(
        'browse.html', reviews=mongo.db.reviews.find())


@app.route('/manage_reviews')
def manage_reviews():
    return render_template(
        'manage.html', reviews=mongo.db.reviews.find())


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('editreview.html', review=the_review)


@app.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
    reviews = mongo.db.reviews
    reviews.update({'_id': ObjectId(review_id)}, {
        'game_title': request.form.get('game_title'),
        'genres': request.form.get('genres'),
        'platforms': request.form.get('platforms'),
        'release_date': request.form.get('release_date'),
        'reviewed_by': request.form.get('reviewed_by'),
        'rating': request.form.get('rating'),
        'review': request.form.get('review')
    })
    return redirect(url_for('manage_reviews'))


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('manage_reviews'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
