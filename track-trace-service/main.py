#main.py file for track & trace service
#FaaS with Google Cloud Functions 

import logging
import os

import numpy as np
import pandas as pd
from google.cloud import storage
import openpyxl

import functions_framework


@functions_framework.http
def cal_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    #the arguments provided in the GET request should be the email (login) & shipmentId
    if request_json and 'arg1' in request_json and 'arg2' in request_json:
        arg1 = request_json['arg1']
        arg2 = request_json['arg2']
    elif request_args and 'arg1' in request_args and 'arg2' in request_args:
        arg1 = request_args['arg1']
        arg2 = request_args['arg2']
    
    #then retrieve the associated status from the database
    status  = retrieve_status(arg1, arg2)

    return 'Status: {}'.format(status)



def retrieve_status(login, package_nr):
    """Background Cloud Function that works with what is in the Cloud Storage.
    """
    project_id = os.environ.get('PROJECT_ID', 'Specified environment variable is not set.')
    bucket_name = os.environ.get('DATA_REPO', 'Specified environment variable is not set.')
    file_name = os.environ.get('FILE_NAME', 'Specified environment variable is not set.')
    print('Project Id: {}'.format(project_id))
    print('Bucket Name: {}'.format(bucket_name))

    #open a channel to read the file from GCS
    client = storage.Client(project=project_id)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    temp_filename = os.path.join('/tmp', file_name)
    blob.download_to_filename(temp_filename)

    #load the excel database from GCS
    dataset = pd.read_excel(temp_filename, dtype={'email': str, 'shipmentId': np.int32, 'status': str})
    package_nr = int(package_nr)
    login = login
    #select the instance based on the shipmentId provided in the GET request
    instance_bool = dataset['shipmentId'] == package_nr
    instance = dataset[instance_bool]
    instance_status = instance["status"]
    #check whether the login matches the correct login
    instance_email = instance["email"]
    if instance_email.item() != login:
        return 'Incorrect login'
    #give the status back to the cal_http function in the correct format
    instance_status = instance_status.item()
    print(instance_status)
    instance_status = str(instance_status)

    #clean up
    os.remove(temp_filename)

    return instance_status
