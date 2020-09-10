# GameReviews 

*"Your home of video game reviews"*

GameReviews is a site for and based around users who want to read and write reviews for their favourite video games and store them all in one place. Use the search function to find and read game reviews or create an account to begin contributing your own.

---

# Contents
1. [UX / Project Goals](#ux)
2. [User Stories](#user-stories)
3. [Site Owner Goals](#site-owner-goals)
4. [Design Choices](#design-choices)
5. [Wireframes](#wireframes)
6. [Features & Potential Future features](#features)
7. [Technologies used](#languages)
8. [Testing](#testing)
9. [Issues and resolutions](#issues-and-resolutions)
10. [Deployment](#deployment)
11. [Credits](#credits)
---

## UX


### Project Goals

The goal of this project is to provide users a place where they can:
* Search for reviews
* Read reviews
* Edit reviews
* Delete reviews
* Create an account

#### User stories

* *“As a gamer I want to be able to read other people’s reviews on games that I'm interested in or that I might play”*
* *“As a gamer I want somewhere to review video games that I’ve played”*
* *“As a user I want to be able edit or delete my reviews incase I make a mistake or my opinion changes“*
* *“As a user I want to login and have a saved collection of my own reviews”*
* *“As a user I want to be able to use a search function to find reviews submitted by other users”*
* *“As a user I want to be able to use this app across various devices e.g desktop/laptop/tablet/mobile”*
* *"As a user I would like the review submission process to be simple and intuitive"*
* *"As a user I want to be able to quickly navigate through the app with ease"*

#### Site Owner Goals

To provide a platform used across various devices for users who want to read and submit video game reviews.

---

## Design Choices

I've opted to use detailed straight lineal colour style icons that are representative of gaming culture throughout the site which act as focal points in the layout and also helps to contextualize what the site is about and who it is aimed at. Shades of white for the background color gives the colourful icons more pop.

* Simple user friendly interface.
* Fixed Navbar featuring app name and flagship logo. Nav links and search function enable easy navigation of the app.
* Muted neutral colours in the layout to compliment the use of detailed straight lineal colour style icons
* Shades of white for the backgrounds #FFFFFF #FAFAFA #F5F5F5
* Jet for font colours #333333 
* For button colours in keeping with the gamepad button colours: French Pink #EF6C8F Dark Orchard #9038A8 Light Sea Green #20BDAD
* Forms fields always occupy left of the screen whilst the right side display icons, pushing below on smaller screen sizes
* Information and search results occupy left side of the screen whilst the right side displays search function and icons, pushing below on smaller screens
* Review pages feature a single image of the game along with some information situated in the top half of the screen with the text area just below it
* [Monfett](https://fonts.google.com/specimen/Monofett?query=mono) is used for 'GameReviews' and some headings whilst everything else is [Roboto](https://fonts.google.com/specimen/Roboto?sidebar.open=true#about)

---

### Wireframes

I used [Balsamiq](https://balsamiq.com/) to create wireframes for **mobile, tablet and desktop.**

You can find my wireframes [here](https://github.com/AlexPullen91/GameReviews/tree/master/wireframes).

---

### Features

This site is designed to provide users a simple and intuitive experience where within just a matter of clicks they are signed up and then writing their review.

This app will utilize the IGDB API to pull information about the games that users search for which then populates the site's database. 

This is to facilitate a positive user experience as they simply type in the name of the game that they're looking for, proceed if they're happy with the selection and then all they have to do is provide a rating and write out their review.

Once users create an account they are are able to submit multiple reviews, edit reviews and delete reviews.

Users are able to search for and read reviews without creating an account and are prompted to create one if they wish to submit reviews.


#### Potential Future features

* Options to purchase games from the review page
* Upvoting / downvoting system or a likes system to indicate quality of or approval of reviews
* More site members features such as forums and messaging
* Customizable user profiles
* Dark mode

---

## Technologies Used

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)

---

### Libraries

* [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Bootstrap](https://getbootstrap.com/)
* [jQuery](https://jquery.com/)
* [Google Fonts](https://fonts.google.com/)

---

### Tools

* [MongoDB](https://www.mongodb.com/)
* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Git](https://git-scm.com/)
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
* [Balsamiq](Balsamiq)

---

## Testing

Testing for responsiveness and bugs throughout development was carried out with google chrome developer tools and the device toolbar to ensure compatibility on all screen sizes.

## Manual Testing

*Test case:* **User sign up process**

This test determines if the user sign up process works as intended

    1. User clicks sign up button on landing page or navbar and is directed to sign up page.
    2. Clicking sign up button at bottom of form alerts user to empty required input fields.
    3. Entering a name in username field that already exists in the database along with matching passwords alerts user to try a different name.
    4. Entering a unique name in username field with passwords that do not match alerts user to try again.
    5. Entering a unique name in username field with matching passwords successfully creates a new user and directs them to their dashboard.

    Verdict: Working as intended

*Test case:* **User login process**

This test determines if the user login process works as intended

    1. User clicks login button on landing page or navbar and is directed to login page.
    2. Clicking login button at bottom of form alerts user to empty required input fields.
    3. Entering a name into username field and a password into password field that aren't in the database alerts user with an error message.
    4. Entering a name into username field that is saved in the database and entering an incorrect password alerts user with an error message.
    5. Entering a name into username field that is saved in the database along with entering the correct password redirects user to their dashboard.

    Verdict: Working as intended

*Test case:* **Site responsive to user session**

This test determines if the site responds to whether or not user is logged in

    1. Upon visiting landing page user can see login and sign up buttons on the left and on the navbar which direct the user to their respective pages.
    2. Upon completing the sign up or login process user is redirected to the dashboard where navbar now displays:
        - 'Dashboard' instead of 'Home'
        - 'Review' now has dropdown functionality with the options 'Browse' and 'Manage'.
        - 'Logout' instead of 'Sign up' or 'Login'
    4. Clicking 'Home' will now take user to 'Dashboard' instead of landing page until they log out.
    5. Clicking 'Browse' still works the same as intended, taking user to browse review page where they can view and select reviews submitted by all users.
    5. Clicking 'Manage' takes user to their review management screen where they can view, edit or delete reviews that only they have submitted.
        - clicking view takes user to review page where they can press either, 'Edit, 'Delete' or 'Go back' buttons.
        - when viewing the review page whilst logged out the user instead sees "Want to submit your own review?" 'Click here'.
        - selecting 'Click here' redirects user to login page with an alert advising to login first. If they are already logged in they are taken straight to add review page.
    6. Clicking 'Logout' in the dashboard screen or in the navbar takes user back to landing page with a success alert and navbar returns to initial state.

    Verdict: Working as intended

*Test case:* **Search Function**

This test determines if the search function works as intended.

    1. User clicks in the search field and types in a game name and presses enter.
    2. If the game name does not exist in the IGDB database (IndexError) they are redirected back to dashboard or landing page with error message, "There were no matches for this game, try something else!"
    3. If the game name returns a (KeyError) in the console, user is redirected back to dashboard or landing page with error message, "There was a problem with your search, try something else!"
    4. If the game name finds a match in the IGDB database user is taken to search.html where a clickable image of the game cover is rendered along with any previously submitted reviews for that game.
    5. If there are no reviews found in the database the search will still fetch the game cover which users can click and begin reviewing. 

    Verdict: Working as intended

*Test case:* **Adding a review**

This test determines if the add review function works as intended.

    1. Once user has searched for a game and are satisfied with their selection they are taken to addreview.html
    2. Here they will see the input fields for title, genres, platforms and released with their values already set (input fields set to readonly).
    3. Below they will see rating and review input fields and below these, Submit and Cancel buttons.
    4. Selecting Submit before choosing a rating alerts user to "please select an item in the list".
    5. Selecting a rating and then selecting Submit button without entering anything in review field alerts user to "Please fill in this field."
    6. Selecting a rating and entering text into the review field followed by selecting Submit button user is redirected to browse.html with a confirmation message above their review.
    7. If user follows these steps whilst already having reviewed the same game they are redirected to dashboard with an error message and the review is not added to database.
    8. Selecting cancel button returns user to browse.

    Verdict: Working as intended


### Issues and Resolutions

* During development I encountered an issue with the user sign up feature when users entered a name already taken in the database.
    * The error handling process would correctly alert the user that the name is already taken but also alert them that their passwords didn't match even when they did.
    * This was solved by redirecting the user to the signup page at the end of each if statement.

* I encountered an issue when working on the search API function that involved trying to grab the game image.
    * The cover.url key in the parameters of the API request would only retern a tiny thumbnail image.
    * This wasn't suitable for my needs so after some digging I found the info I needed in the API documentation.
    * Within the url string returned from the API the image size is determined by ```"thumb"```.
    * Using ```replace()``` to swap in ```cover_big``` I now had the url for the larger image.

* A particularly gruesome nuisance during development was coding in the logic to stop users submitting reviews for a game they had already reviewed.
    * Much of the headache was born through trying to locate the values I needed from the appropriate keys.
    * Liberal use of ```print()``` in the console helped me narrow down what I needed and eventually I was left with ```user``` and ```existing_review```
    * ```user``` contains the value received from the user database collection and ```existing_review``` contained the value obtained from the review database collection.
    * I tried these variables, (including earlier *wrong* variations of them) in various different conditionals before settling on the current solution.
    * Before there is a particular review in the database for a user then ```existing_review``` returns ```None```, once I realised this I stopped checking in the first ```if``` condition for ```existing_review['reviewed_by'] is None``` which was returning ```TypeError: 'NoneType' object is not subscriptable```.
    * By just checking ```if user and existing_review is None``` the code block that inserts the review runs.
    * Following this up with ```elif user and existing_review['reviewed_by']``` users are successfully redirected without submitting a review, error message and all.
    * Perhaps not the most elegant piece of code or the optimal user experience but the simple fact that it works is a satisfactory trade off for the time being.

* When reviews are submitted with any formatting this is recorded appropriately in the database but is lost when rendered by the Jinja templating.
    * By keeping ```<textarea>``` set to readonly as the container for the review text the original formatting is retained.

### Known Issues

* *Currently users are still able to post reviews for a game they have already submitted a review for* **solved**
* *Reviews submitted to the database retain their formatting but when rendered through jinja templating they lose it.* **solved** 

---

## Deployment


---

---

## Credits


### Content

* Icons used are from [Flaticon](https://www.flaticon.com/packs/gaming-98?word=gaming)

### Code

* The [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) youtube channel was extremely helpful for learning how to implement some Flask features such as the user login system and flash messaging.

### Acknowledgements

* My mentor [Simen Daehlin](https://github.com/Eventyret) for his help and advice on this project.

### Disclaimer

*This site is intended for educational purposes only.*
