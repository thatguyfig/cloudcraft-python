# CLOUDCRAFT.PY 
# 
# Stores all cloudcraft specific functions and objects

import requests
import json
from .utils import build_auth_header

def add_aws_account(api_key: str, name: str, roleArn: str):
    
    """Register a new AWS account with Cloudcraft, for visualisation via the API."""
    
    # define the url we will be targetting
    url = 'https://api.cloudcraft.co/aws/account'
    
    # build auth header
    header = build_auth_header(api_key)
    
    # add the content type header
    header['Content-Type'] = 'application/json'
    
    # build the json payload
    payload = {
        "name": name,
        "roleArn": roleArn
    }
    
    # create json object
    payload_json = json.loads(payload)
    
    # send post request
    response = requests.post(
        url=url,
        headers=header,
        data=payload_json
    )
    
    return response
    
    
def get_aws_accounts(api_key: str):
    
    """Lists all the visible AWS accounts in CloudCraft"""
    
    # define the url we will be targetting
    url = 'https://api.cloudcraft.co/aws/account'
    
    # build auth header
    header = build_auth_header(api_key)
    
    # send request
    response = requests.get(url=url, headers=header)
    
    return response

