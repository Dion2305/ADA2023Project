## General info
This service handles the payments of users for their subscriptions. It will take bank information and will interact with the accountsAPI when the transaction has been successful
	
## Files
The service is created with:
* requirement.txt that sets the required python packages for the service.
* daos/payment_dao.py contains the format for storing payment related details in a payment database
* resources/payment.py has the functions "pay". Which adds the payment information and time of payment to a user database if the transaction is successful. It will then fire a request to the accountsAPI to change the subscribed user status.
* Dockerfile contains all the commands needed to run the app
* app.py holds the app routes for these functions
* requirements.txt holds the required packages to run the application
	
## Setup
To run the service, the Dockerfile needs to be build and hosted on a port (this will be done using docker-compose in our project). Then, via the app routes, the functions can be called with given parameters (e.g. via Insomnia).
