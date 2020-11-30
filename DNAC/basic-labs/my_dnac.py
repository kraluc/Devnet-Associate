import json, sys
import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, USERNAME, PASSWORD, VERSION
from netaddr import *


URL = "https://sandboxdnac.cisco.com"


def get_auth_token(url:str=URL):
    """
    Building out Auth request. Using requests.post to call the Auth Endpoint
    """
    urn = '/dna/system/api/v1/auth/token'
    resp = requests.post(url + urn, auth=HTTPBasicAuth(USERNAME, PASSWORD))  # POST request
    token = resp.json()['Token']  # retrieve the Token from the returned JSON
    print(f'Token Retrieved: {token}')  # print out the Token
    return token


def get_device_list(ip:str='10.10.22.66', mac:str='f8:7b:20:67:62:80', url:str=URL):

    token = get_auth_token()
    urn = '/api/v1/network-device'

    # Build header info
    hdr = {
        'x-auth-token' : token,
        'Content-Type' : 'application/json'
        }  # Build header info

    # Build query based on IP and mac address (check that they are valid)
    try:
        querystring = {
            'managementIPAddress' : str(IPAddress(ip)),
            'macAddress' : str(EUI(mac, dialect=mac_unix_expanded))
            }
    except AddrFormatError(f'IP {ip} or/and MAC {mac} is/are invalid'):
        sys.exit(0)

    resp = requests.get(url + urn, headers=hdr, params = querystring)
    print(f'\n\nresponse code: {resp.status_code}\n\n')

    device_list = resp.json()
    print(json.dumps(device_list, sort_keys=True, indent=4))  # Pretty print the data


if __name__ == "__main__":
    get_device_list()
