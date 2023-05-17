## General info
This service connects with an external shipping service and retrieves the status of a package based on a shipmentId and login email.
The main.py connects with the Google Cloud Console and can be used to create a Function as a Service setup.
	
## Files
The service is created with:
* requirement.txt that sets the required python packages for the service.
* env.yaml file that sets the environment variables.
* main.py that sets up a function triggered by an http request, that can retrieve a shipment status
	
## Setup
To run this service from a VSCode terminal:

```
$ cd .../track-trace-service
$ gcloud auth login
$ gcloud config set project ada-group2
$ gcloud functions deploy cal_http --runtime python310 --region=us-central1 --entry-point=cal_http --trigger-http --env-vars-file env.yaml --allow-unauthenticated
$ gcloud functions describe cal_http
```
Then the trigger URL can be used in a web browser as follows your_trigger_url?arg1={email}&arg2={shipmentId}
e.g. https://us-central1-ada-group2.cloudfunctions.net/cal_http?arg1=person6&arg2=3856 gives 'Status: shipped'
