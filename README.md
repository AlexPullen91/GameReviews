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
* [Monfett](https://fonts.google.com/specimen/Monofett?query=mono) is used for 'GameReviews' whilst the sans-serif [Roboto](https://fonts.google.com/specimen/Roboto?category=Sans+Serif,Monospace#standard-styles) is used everywhere else

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



---

### Libraries



---

### Tools


---

## Testing



## Manual Testing



### Issues and Resolutions

* Fixed an issue with sign up where users entering a name that already exists in the database would also be told their passwords dont match when they did. This was solved by adding a return redirect after each error message.

### Known Issues



---

## Deployment


---

---

## Credits


### Content



### Code


### Acknowledgements



### Disclaimer

*This site is intended for educational purposes only.*
