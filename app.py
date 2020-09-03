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


@APP.route('/browse-reviews')
def browse_reviews():
    """
    Renders the browse reviews page and retreives reviews
    from the database
    """
    return render_template(
        'pages/browse.html', reviews=MONGO.db.reviews.find())


@APP.route('/review/<review_id>')
def get_review(review_id):
    """
    Retrieves a specific review from the database and
    renders it on review.html
    """
    the_review = MONGO.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('pages/review.html', review=the_review)


@APP.route('/add-review')
def add_review():
    """
    Checks if user is logged in, if yes they are sent to add review page
    if user is not logged in they are redirected to login page
    """
    if 'username' in session:
        return render_template(
            'pages/addreview.html', reviews=MONGO.db.reviews.find())
    flash("You must create an account or login to submit reviews!", "nouser")
    return redirect('login')


@APP.route('/insert-review', methods=['POST'])
def insert_review():
    """
    Inserts user's review into the reviews database then
    redirects user to browse.html
    """
    reviews = MONGO.db.reviews
    reviews.insert_one(request.form.to_dict())
    flash("Your review has been added, nice!", "added")
    return redirect(url_for('browse_reviews'))


@APP.route('/manage-reviews')
def manage_reviews():
    """
    If user is logged in then renders the manage review page which
    only lists reviews submitted by that user
    if user is not logged in they're redirected to the login page
    """
    if 'username' in session:
        return render_template(
            'pages/manage.html', reviews=MONGO.db.reviews.find())
    flash("You must create an account or login first!", "noaccount")
    return redirect('login')


@APP.route('/edit-review/<review_id>')
def edit_review(review_id):
    """
    Grabs selected review from the database and renders it
    on the edit review page
    """
    the_review = MONGO.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('pages/editreview.html', review=the_review)


@APP.route('/update-review/<review_id>', methods=['POST'])
def update_review(review_id):
    """
    Any edits made by the user are recorded and saved in the database
    and they are redirected to the manage review page
    """
    reviews = MONGO.db.reviews
    reviews.update({'_id': ObjectId(review_id)}, {
        'game_title': request.form.get('game_title'),
        'genres': request.form.get('genres'),
        'platforms': request.form.get('platforms'),
        'release_date': request.form.get('release_date'),
        'reviewed_by': request.form.get('reviewed_by'),
        'image_url': request.form.get('image_url'),
        'rating': request.form.get('rating'),
        'review': request.form.get('review')
    })
    flash("Changes saved", "saved")
    return redirect(url_for('manage_reviews'))


@APP.route('/delete-review/<review_id>')
def delete_review(review_id):
    """
    Removes the selected review from the database and
    redirets user to manage reviews
    """
    MONGO.db.reviews.remove({'_id': ObjectId(review_id)})
    flash("Deleted successfully", "deleted")
    return redirect(url_for('manage_reviews'))


@APP.route('/signup', methods=['POST', 'GET'])
def signup():
    """
    Handles new user sign up process, if passwords match and theres no
    existing user then they're added to the database, logged in and
    redirected to the dashboard
    """
    if request.method == 'GET':
        return render_template('pages/signup.html')

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
                return redirect(url_for('dashboard'))
            flash("Username already exists! Try another!", "userexists")
            return redirect(url_for('signup'))
        flash("Your passwords do not match! Try again!", "nomatch")
        return redirect(url_for('signup'))
    return render_template('pages/signup.html')


@APP.route('/login', methods=['POST', 'GET'])
def login():
    """
    User login process, username is retrieved from the database and
    if correct password is used they're redirected to their dashboard
    """
    if request.method == 'GET':
        return render_template('pages/login.html')

    users = MONGO.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode(
                'utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
    flash("Invalid username / password combination", "invalid")
    return redirect('/login')


@APP.route('/dashboard')
def dashboard():
    """
    Renders the dashboard page
    """
    return render_template('pages/dashboard.html')


@APP.route('/logout')
def logout():
    """
    User is logged out by clearing the session
    """
    session.clear()
    flash("Logged out, Bye!", "logout")
    return redirect('/')


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
