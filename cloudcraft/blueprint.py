# BLUEPRINT.PY
#
# All blueprint specific functions

import requests
import json
from .utils import save_byte_file, save_json_file, load_json_file, build_auth_header, get_json, check_auth_error

def get_blueprint_by_name(blueprint_name: str, api_key: str):

    """Checks for the existence of a blueprint for a given name. Returns true if it does."""

    # a counter for the number of blueprints that match our target
    matching_blueprints = []

    # list all blueprints
    response = list_blueprints(api_key)

    # decode to utf8
    response = str(response.content, encoding='utf8')

    # load to json
    json_response = json.loads(response)

    # iterate over blueprints
    for blueprint in json_response['blueprints']:
        
        # if we find a matching blueprint
        if blueprint['name'] == blueprint_name:


            # build an object with all the values
            matching_blueprint = {
                'name': blueprint['name'],
                'id': blueprint['id'],
                'readAccess': blueprint['readAccess'],
                'writeAccess': blueprint['writeAccess'],
                'createdAt': blueprint['createdAt'],
                'updatedAt': blueprint['updatedAt'],
                'CreatorId': blueprint['CreatorId'],
                'LastUserId': blueprint['LastUserId']
            }

            # add it to the list
            matching_blueprints.append(matching_blueprint)

    # if we have a matching blueprint
    if len(matching_blueprints) > 0:

        return matching_blueprints

    # if nothing was found
    else:

        return None
             



    

    


def list_blueprints(api_key):
    
    """Gets all the blueprints in the CloudCraft account"""

    # build request url
    url = 'https://api.cloudcraft.co/blueprint'

    # build auth header
    header = build_auth_header(api_key)

    # send request
    response = requests.get(
        url=url,
        headers=header
    )
    
    # check if there is any issue with auth
    check_auth_error(response)

    return response

def export_blueprint(api_key, bp_id, export_format, save=True, filename=None):
    
    """Gets the current blueprint for a given Blueprint ID"""
    
    # list of valid formats allowed
    valid_export_formats = ['svg', 'png', 'pdf', 'mxGraph', 'json']
    
    # validate format
    if export_format not in valid_export_formats:
        print('Please provide a supported exported format such as:')
        print(', '.join(valid_export_formats))
    
    # otherwise
    else:
        
        # build auth header    
        header = build_auth_header(api_key)

        # build request url 
        url = 'https://api.cloudcraft.co/blueprint/{0}/{1}'.format(bp_id, export_format)
        
        # send request
        response = requests.get(
            url=url,
            headers=header
        )
        
        # if saving is enabled
        if save:
            
            # if a filename was supplied
            if filename:
                
                # use it
                filename = '{0}.{1}'.format(filename, export_format)
                
            # otherwise
            else:
                
                # build one using the blueprint id
                filename = '{0}.{1}'.format(bp_id, export_format)
            
            if export_format == 'json':
                
                # save the file
                save_json_file(filename, response.content)
            
            else:

                # save the file
                save_byte_file(filename, response.content)
            
        return response

def update_blueprint(api_key, bp_id, json_body):
    
    """Updates the JSON blueprint of a given Blueprint ID"""
    
    # build request url
    url = 'https://api.cloudcraft.co/blueprint/{}'.format(bp_id)

    # build auth header + content-type
    header = build_auth_header(api_key)
    
    # add the content type header
    header['Content-Type'] = 'application/json'    
    
    # if the 'id' is present
    if 'id' in json_body:
        
        # remove it
        json_body.pop('id')

    # create json obj
    json_body = json.dumps(json_body)
    
    # send put with json 
    response = requests.put(
        url=url,
        headers=header,
        data=json_body
    )
    
    return response

def delete_blueprint(api_key, bp_id):
    
    """Deletes the blueprint from the provided blueprint ID"""
    
    # build the url
    url = 'https://api.cloudcraft.co/blueprint/{}'.format(bp_id)

    # build the headers
    header = build_auth_header(api_key)
    
    # send the delete request
    response = requests.delete(
        url=url,
        headers=header
    )

    return response

def build_blueprint_schema(name):
    
    """Returns a dictionary of the correct schema ready to create a blueprint with"""
    

    # create the schema with the provided name
    data = {
        'data': {
            'grid': 'standard',
            'name': name
        }
    }
        
    return data

def get_blueprint_layout(api_key, bp_id, save=True):
    
    """Gets the layout of the blueprint in JSON output"""

    # build request url
    url = 'https://api.cloudcraft.co/blueprint/{}'.format(bp_id)

    # build auth header
    header = build_auth_header(api_key)

    # send request
    response = requests.get(
        url=url,
        headers=header
    )
    
    # if saving enabled
    if save:
        
        # create a filename
        filename = 'output/json/target-blueprint-layout.json'
        
        # turn response to json object
        response_json = get_json(response.content)
        
        # save json to file with identation
        with open(filename, 'w') as f:
            json.dump(response_json, f, indent=4)
            f.close()

    return response


def create_blueprint(api_key, json_body):
    
    """Creates a new blueprint from the provided JSON object"""
    
    # build base url
    url = 'https://api.cloudcraft.co/blueprint/'

    # build auth header
    header = build_auth_header(api_key)
    
    # add the content type header
    header['Content-Type'] = 'application/json'
    
    # create JSON object
    json_body = json.dumps(json_body)

    # send post request
    response = requests.post(
        url=url,
        headers=header,
        data=json_body
    )
    
    return response

def load_blueprint_from_disk(filepath):

    file_content = load_json_file(filename=filepath)

    return file_content