# UTILS.PY
#
# Utility functions that are used throughout the application and have no specific external dependencies.

import json
import time
import datetime
import os

def check_auth_error(response: object) -> None:

    """Checks the response status code for invalid codes"""

    # if a 401 is received, the client is not authenticated
    if response.status_code == 401:
        
        raise PermissionError('Your API token is incorrect. Please try again')
        return


def build_auth_header(api_key: str) -> dict:

    """Builds the authentication header"""
    
    header = {
        'Authorization': 'Bearer {}'.format(api_key)
    }
    
    return header

def save_json_file(filename: str, data) -> None:
    
    """Saves provided JSON data to the provided filepath"""

    # if file already exists
    if os.path.exists(filename):
        
        # remove the file
        os.remove(filename)
    
    # open lid
    with open(filename, 'w') as f:
        
        # json dump
        json.dump(data, f, indent=4, default=default(data))
        
        # close lid
        f.close()

def load_json_file(filename: str) -> dict:

    """Loads a JSON blueprint file from the provided filepath"""

    # if the file exists
    if os.path.exists(filename):

        # load it
        with open(filename, 'r') as f:
            
            # load the json data
            data = json.loads(f.read())

            # close file
            f.close()

        return data

    # otherwise
    else:
        raise FileNotFoundError()
    

def save_byte_file(filename: str, data) -> None:
    
    """Saves provided byte data to the provided filepath"""

    # if the file already exists
    if os.path.exists(filename):

        # remove the file
        os.remove(filename)
    
    try:
        # open lid
        with open(filename, 'wb') as f:
            
            # byte dump
            f.write(data)
            
            # close lid
            f.close()

    except Exception as e:
        print(e)


def get_json(x: bytes):
    
    """Converts data object into JSON object, from a response object"""
    x_json = json.loads(x)
    
    return x_json

def pretty_print(x: object) -> None:
    
    """Prints data with a 4-space indent - pretty-like"""
    
    print(json.dumps(x, indent=4))

def wait(x: int) -> None:
    
    """Pauses the execution of the program for the provided seconds."""
    
    time.sleep(int(x))
    
def default(o: dict) -> str:
    
    """Overcomes JSON serialisation problems with dates from AWS that contain 'T' + 'Z'"""
    
    if isinstance(o, (datetime.datetime)):
        return o.__str__()

def extract_customers(data: dict) -> dict:
    
    """Extracts the customer data from the DynamoDB results"""
    
    # temp array for return
    customers = {
        'customers': []
    }
    
    # iterate over all records
    for item in data['Items']:
        
        # build the singular customer item
        customer = {
            "name": item['customerName']['S'],
            "region": item['customerRegion']['S']
        }
        
        # add it to the list
        customers['customers'].append(customer)
        
    return customers

def build_dir(path: str) -> None:
    
    """Created a directory of the provided path if it does not already exist"""
    
    # if the path doesnt exist
    if not os.path.exists(path):
        
        # make it
        os.makedirs(path)