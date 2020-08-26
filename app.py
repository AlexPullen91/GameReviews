import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/landing_page')
def landing_page():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('landingpage.html')


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


@app.route('/signup_page')
def signup_page():
    return render_template('signup.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            if existing_user is None:
                hashpass = bcrypt.hashpw(
                    request.form['password'].encode('utf-8'), bcrypt.gensalt())
                users.insert({
                    'name': request.form['username'],
                    'password': hashpass
                })
                session['username'] = request.form['username']
                return redirect(url_for('login_page'))
            return ('That username already exists!')
        return ('Your passwords do not match')
    return render_template('signup.html')


@app.route('/login_page')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('userhub'))
    return 'Invalid username/password combination'


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/landing_page')


@app.route('/userhub')
def userhub():
    return render_template('userhub.html', users=mongo.db.users.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
