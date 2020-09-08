import os
from flask import Flask, render_template, redirect, request, url_for, session,\
     flash
from flask_pymongo import PyMongo
import bcrypt
import requests
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

APP = Flask(__name__)

APP.config["MONGO_URI"] = os.environ.get("MONGO_URI")
APP.secret_key = os.environ.get("SECRET_KEY")
API_KEY = os.environ.get("API_KEY")

MONGO = PyMongo(APP)


@APP.route('/')
def landing_page():
    """
    If user is not logged in, renders the landing page
    if user is logged in, redirects to dashboard
    """
    if 'username' in session:
        return redirect('dashboard')
    return render_template('pages/landingpage.html')


@APP.route('/search', methods=['POST', 'GET'])
def search_game():
    """
    Makes a POST request to the IGDB API using a user inputted value and
    the data is passed into form fields in search.html ready for user to
    rate, review and then submit. Redirects to landing page or dashboard
    upon encountering errors.
    """
    if request.method == 'POST':
        games_url = 'https://api-v3.igdb.com/games'
        headers = {'user-key': API_KEY}
        gameName = request.form.get('search')
        games_params = {
            'fields': 'name, genres.name, platforms.name, release_dates.human, cover.url',
            'search': f"{gameName}",
            'limit': 1
                }

        r = requests.post(games_url, headers=headers, params=games_params)

        try:
            cover = r.json()[0]['cover']['url']
            coverBig = cover.replace('thumb', 'cover_big')
            gameTitle = r.json()[0]['name']
            genres = r.json()[0]['genres']
            genreNames = []
            for name in genres:
                genreNames.append((name['name']))

            platforms = r.json()[0]['platforms']
            platformNames = []
            for name in platforms:
                platformNames.append((name['name']))

            release_date = r.json()[0]['release_dates']
            release_dates = []
            for human in release_date:
                release_dates.append((human['human']))

            return render_template(
                'pages/search.html',
                coverBig=coverBig,
                gameTitle=gameTitle,
                genreNames=genreNames,
                platformNames=platformNames,
                release_dates=release_dates
                )
        except KeyError:
            flash("There was a problem with your search, try something else!", "prob")
            return redirect('dashboard')
        except IndexError:
            flash("There were no matches for this game, try something else!", "nogame")
            return redirect('dashboard')
    if request.method == 'GET':
        return redirect('/')


@APP.route('/searchreview', methods=['POST'])
def search_reviews():
    if request.method == 'POST':
        reviewName = request.form.get('searchreviews')
        # the_review = MONGO.db.reviews.find({'game_title': f"{reviewName}"})
        reviews = MONGO.db.reviews
        reviewList = list(reviews.find({'game_title': f"{reviewName}"}))
        id_list = []
        for _id in reviewList:
            id_list.append((_id['_id']))
        game_title = reviewList[0]['game_title']
        print(game_title)
        return render_template(
            'pages/searchreviews.html',
            reviewList=reviewList,
            game_title=game_title,
            reviews=MONGO.db.reviews.find()
            )
    return redirect('/')


@APP.route('/browse/reviews')
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


@APP.route('/addreview', methods=['POST'])
def add_review():
    """
    Checks if user is logged in, if yes they are sent to add review page
    if user is not logged in they are redirected to login page
    """
    if 'username' in session:
        coverBig = request.form.get('coverBig')
        gameTitle = request.form.get('gameTitle')
        genreNames = request.form.get('genreNames')
        platformNames = request.form.get('platformNames')
        release_dates = request.form.get('release_dates')
        return render_template(
            'pages/addreview.html',
            coverBig=coverBig,
            gameTitle=gameTitle,
            genreNames=genreNames,
            platformNames=platformNames,
            release_dates=release_dates,
            reviews=MONGO.db.reviews.find())
    flash("You must create an account or login to submit reviews!", "nouser")
    return redirect('login')


@APP.route('/insert/review', methods=['POST'])
def insert_review():
    """
    Inserts user's review into the reviews database then
    redirects user to browse.html
    """
    reviews = MONGO.db.reviews
    reviews.insert_one(request.form.to_dict())
    flash("Your review has been added, nice!", "added")
    return redirect(url_for('browse_reviews'))


@APP.route('/manage/reviews')
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


@APP.route('/edit/review/<review_id>')
def edit_review(review_id):
    """
    Grabs selected review from the database and renders it
    on the edit review page
    """
    the_review = MONGO.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('pages/editreview.html', review=the_review)


@APP.route('/update/review/<review_id>', methods=['POST'])
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


@APP.route('/delete/review/<review_id>')
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

    if request.method == 'GET':
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
    flash("Logged out... Bye!", "logout")
    return redirect('/')


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
