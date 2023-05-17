## General info
This repository contains code to realise 5 microservices that can be deployed using orchestration with Kubernetes. 
	
## Files
Each folder contains everything that is needed to build one of the microservices.
* account_management_service corresponds with the account_management service in the Accounts bounded context.
* app_interaction_service corresponds with the service of the same name in the Beers bounded context.
* payment_handling_service corresponds with the service in the Subscriptions bounded context.
* shippingservice corresponds with the service in the Shipping bounded context.
* track-trace-service corresponds with the Track and Trace service function as shown in the deployment diagram.
	
## Setup
Before the Kubernetes deployment can start, the Google Cloud Function from the track-trace-service needs to be created.
The process for this is explained in the README in the folder for that service.

Then, the kubernetes cluster can be deployed by completing the following steps:
* Create a trigger with cloudbuild_ml_components to build the docker containers
* Create a kubernetes cluster in google cloud
* In this cluster clone the repository
* cd to the manifests folder
* run "kubectl apply -f ." to start the pods
* run "kubectl get services --namespace=myapps"
* You can now use the external ips to run the functions in for example insomnia

The app can also be run without using kubernetes. This method uses docker compose in a virtual machine. 
* git clone in a vm
* cd to ADA2023Project
* sudo docker-compose up -d --build
* You can now run all the methods described in the readme files


A user can check the status of their shipment by pasting the shipmentId and login (email) they received
in the following URL:
your_trigger_url?arg1={email}&arg2={shipmentId}
-> https://us-central1-ada-group2.cloudfunctions.net/cal_http?arg1=person6&arg2=3856
