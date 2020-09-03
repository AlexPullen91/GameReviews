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
* [Monfett](https://fonts.google.com/specimen/Monofett?query=mono) is used for 'GameReviews' whilst the sans-serif [Montserrat](https://fonts.google.com/specimen/Montserrat?query=mon#about) is used everywhere else

---

### Wireframes

I used [Balsamiq](https://balsamiq.com/) to create wireframes for **mobile, tablet and desktop.**

You can find my wireframes [here](https://github.com/AlexPullen91/GameReviews/tree/master/wireframes).

---

### Features

This site is designed to provide users a simple and intuitive experience where within just a matter of clicks they are signed up and then writing their review.

This app will utilize the IGDB API to pull information about the games that users search for which then populates the site's database. 

This is to facilitate a positive user experience as they simply type in the name of the game that they're looking for, proceed if they're happy with the selection and then all they have to do is provide a rating out of 5 and write out their review.

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

### Issues and Resolutions

* During development I encountered an issue with the user sign up feature when users entered a name already taken in the database.
    * The error handling process would correctly alert the user that the name is already taken but also alert them that their passwords didn't match even when they did.
    * This was solved by redirecting the user to the signup page at the end of each if statement.


### Known Issues

* Currently users are still able to post reviews for a game they have already submitted a review for.

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
