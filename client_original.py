# Imports
import requests
from requests.auth import HTTPBasicAuth
import base64

# Variables
URL = 'http://dev.web.local'
REQUEST_RETRIES = 3
WAIT_FOR_RETRY = 1
USERNAME = 'cisco'
PASSWORD = '1234QWer'

## Send request
def send_request(url, data, headers):
    tries = 0
    while True:
        tries += 1
        try:
            response = requests.post(url=url, json=data, headers=headers)

            # Everything ok?


            # Raise HTTP error if occurs


        # Network timeout, should we retry?
        except:
            pass

# Encode string to base64
def to_base64(s):
    return base64.b64encode(s.encode('utf8')).decode('utf8')

## Basic auth
def basic_auth():
    url = URL + '/login'
    #creds =
    #headers =
    #response =
    print(response)
    #return response.get('')

## API Key auth
def invoke_info_v1(api_key, name):
    #url = URL + '/v1/info'
    #data =
    #headers =
    #response =
    print(response)
    #return response.get('')

## Bearer token
def invoke_info_v2(bearer_token, name):
    #url = URL + '/v2/info'
    #data =
    #headers =
    #response =
    print(response)

if __name__ == '__main__':
    print('Basic Auth')
    #api_key = basic_auth()

    print('------------------------------------------')

    print('API Key Auth')
    #bearer_token = invoke_info_v1(api_key, )

    print('------------------------------------------')

    print('Bearer Token Auth')
    #invoke_info_v2(bearer_token, )