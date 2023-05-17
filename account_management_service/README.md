## General info
This service handles all accounts registering, logins, authentication, shipping details and interactions between other microservices
	
## Files
The service is created with:
* requirement.txt that sets the required python packages for the service.
* daos/user_dao.py contains the format for storing user related details in a user database
* resources/accountapi.py has the function "create", "get", "login", "changepassword" "removeaccounts", "addshippinginformation", "get_user" and "change_payed_status". Create functions registers a user, login gives an authentication token, get verifies the token and outputs user details, changepassword changes the password, removeaccount removes the user account from the database, addshippinginformation lets the user add their address for shipping, get_user and change_payed are interaction functions with other microservices and gather user id and change the user.subscribed boolean.
* Dockerfile contains all the commands needed to run the app
* app.py holds the app routes for these functions
* requirements.txt holds the required packages to run the application
	
## Setup
To run the service, the Dockerfile needs to be build and hosted on a port (this will be done using docker-compose in our project). Then, via the app routes, the functions can be called with given parameters (e.g. via Insomnia).
