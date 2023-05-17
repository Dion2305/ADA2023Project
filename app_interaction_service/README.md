## General info
This service handles the basic interactions users can have with the app. Users can add beers, retrieve info and details about beers in the database, and delete discontinued beers. Furthermore, they can write reviews, retrieve all reviews and ratings for a beer
	
## Files
The service is created with:
* requirements.txt that sets the required python packages for the service.
* daos/beers_dao.py contains the format for storing beer instance related details in a beer database table (beer id, name, country of origin, type and IBU)
* daos/packages_dao.py contains the format for storing beer package related details in a package database table (package id, date of creation and 6 beer id's of beers in the beer table)
* daos/reviews_dao.py contains the format for storing beer reviews and ratings related to a specific beer id in a reviews database table (review id, user name, rating, and text review)
* resources/app_beers.py, containing all functions related to beer instances
* resources/app_reviews.py, containing all functions related to beer reviews
* resources/packages.py, containing all functions related to packages
* Dockerfile contains all the commands needed to run the app
* app.py holds the app routes for all functions for this service
* db.py initializes the database with all three tables for this service
	
## Setup
To run the service, the Dockerfile needs to be build and hosted on a port (this will be done using docker-compose or k8s in our project). Then, via the app routes, the functions can be called with given parameters (e.g. via Insomnia).


## Functions / Methods
### Beers
* POST | path: /beers: Add a new beer instance to the database of beer. Required details in JSON format: _beer_name, country_of_origin, beer_type and ibu_.
* GET | path: /beers/<beer_id>: Retrieve details of a specific beer instance. Requires a beer_id as argument.
* DELETE | path: /beers/<beer_id>: Remove a beer if it is discontinued from the database.

### Reviews
* POST | path: /reviews: Add a new review and rating to the review database. Required details in JSON format: _beer_id, name, rating (integer 1-5) and review (max. 1024 tokens)_. Reviews can only be written for beers existing in the beer database.
* GET | path: /reviews/<review_id>: Retrieve all reviews of users of a specific beer instance given its beer_id. Also returns the average rating and the date the reviews were written.
* DELETE | path: /reviews/<review_id>: Delete a review and rating using a review_id.

### Packages
* POST | path: /packages: Create a package of six beers that exist in the beer database. Required details in JSON format: _beer_id1, beer_id2, beer_id3, beer_id4, beer_id5, beer_id6_.
* GET | path: /packages/<package_id> Get info on the beers that are in a specific package along with the date the package was created.
* DELETE | path: /packages/<package_id> Delete a beer package.
