import os
from flask import Flask, render_template, redirect, request, url_for, session,\
     flash
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

APP = Flask(__name__)

APP.config["MONGO_URI"] = os.environ.get("MONGO_URI")
APP.secret_key = os.environ.get("SECRET_KEY")

MONGO = PyMongo(APP)


@APP.route('/')
def landing_page():
    """
    Renders the landing page
    """
    return render_template('pages/landingpage.html')


@APP.route('/review/<review_id>')
def get_review(review_id):
    """
    Retrieves a specific review from the database and
    renders it on review.html
    """
    the_review = MONGO.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('pages/review.html', review=the_review)


@APP.route('/add_review')
def add_review():
    """
    Checks if user is logged in, if yes they are sent to add review page
    if user is not logged in they are redirected to login page
    """
    if 'username' in session:
        return render_template(
            'pages/addreview.html', reviews=MONGO.db.reviews.find())
    flash('You must create an account or login to submit reviews', 'noaccount')
    return redirect('login_page')


@APP.route('/insert_review', methods=['POST'])
def insert_review():
    reviews = MONGO.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('pages/browse_reviews'))


@APP.route('/browse_reviews')
def browse_reviews():
    return render_template(
        'pages/browse.html', reviews=MONGO.db.reviews.find())


@APP.route('/manage_reviews')
def manage_reviews():
    if 'username' in session:
        return render_template(
            'pages/manage.html', reviews=MONGO.db.reviews.find())
    flash('You must create an account or login first!', 'noaccount')
    return redirect('login_page')


@APP.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = MONGO.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('pages/editreview.html', review=the_review)


@APP.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
    reviews = MONGO.db.reviews
    reviews.update({'_id': ObjectId(review_id)}, {
        'game_title': request.form.get('game_title'),
        'genres': request.form.get('genres'),
        'platforms': request.form.get('platforms'),
        'release_date': request.form.get('release_date'),
        'reviewed_by': request.form.get('reviewed_by'),
        'rating': request.form.get('rating'),
        'review': request.form.get('review')
    })
    return redirect(url_for('pages/manage_reviews'))


@APP.route('/delete_review/<review_id>')
def delete_review(review_id):
    MONGO.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('pages/manage_reviews'))


@APP.route('/signup_page')
def signup_page():
    return render_template('pages/signup.html')


@APP.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = MONGO.db.users
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
                flash('Sign up successful', 'signedup')
                return redirect(url_for('login_page'))
            flash('That username already exists!', 'userexists')
            return redirect(url_for('signup_page'))
        flash('Your passwords do not match', 'nomatch')
        return redirect(url_for('signup_page'))
    return render_template('pages/signup.html')


@APP.route('/login_page')
def login_page():
    return render_template('pages/login.html')


@APP.route('/login', methods=['POST'])
def login():
    users = MONGO.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode(
                'utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
    flash('Invalid username / password combination', 'invalid')
    return redirect('/login_page')


@APP.route('/logout')
def logout():
    session.clear()
    flash('Logout successful', 'logout')
    return redirect('/')


@APP.route('/dashboard')
def dashboard():
    return render_template('pages/dashboard.html')


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
