## General info
This service creates the shipping information by connecting a user to a beer package. This information is then send to a third party service which handles the shipment.
	
## Files
The service is created with:
* requirement.txt that sets the required python packages for the service.
* daos/shipping_dao.py contains the format for storing shipping related details in a shipping database
* resources/shipment.py has the functions "create_shipment", "get_user_data" and "get_package_data". "create_shipment" creates the shipment if a user exists, the user payed and the beer package exists. "get_user_data" gets the data from the account_management_service. "get_package_data" gets the data from the app_interaction_service
* Dockerfile contains all the commands needed to run the app
* app.py holds the app routes for these functions
* requirements.txt holds the required packages to run the application
	
## Setup
To run the service, the Dockerfile needs to be build and hosted on a port (this will be done using docker-compose in our project). Then, via the app routes, the functions can be called with given parameters (e.g. via Insomnia).
