import requests
import json

from .utils import build_dir, save_byte_file, save_json_file, build_auth_header

def snapshot_aws_region(api_key: str, account_id: str, aws_region: str, export_format: str, filter_string: str, excluded_types: list, scale=1, auto_connect=True, projection='isometric', grid=False, save=True, label=True, transparent=True):

    """Exports a snapshot of an AWS region for the provided customer name in the provided format for the provided filter string"""

    # build the absolute base url
    url = 'https://api.cloudcraft.co/aws/account/{0}/{1}/{2}'.format(account_id, aws_region, export_format)

    # create optional parameters
    parameters = '?' # beginning params
    parameters = parameters + 'grid=' + str(grid) # show grid or not
    parameters = parameters + '&autoConnectComponents=' + str(auto_connect) # connect components or not
    parameters = parameters + '&filter=' + filter_string # the string to filter components matching with
    parameters = parameters + '&scale=' + str(scale)  # the scale of the output diagram (0.5 - half, 2 - double)
    parameters = parameters + '&projection=' + projection # projection type - 'isometric' / '2d'
    parameters = parameters + '&exclude=' + ','.join(excluded_types) # the types of objects to filter out
    parameters = parameters + '&label=' + str(label) # whether to label the items or not
    parameters = parameters + '&transparent=' + str(transparent) # whether background is transparent

    # add url and parameters
    full_url = url + parameters

    # create auth headers
    header = build_auth_header(api_key)

    # send request
    response = requests.get(url=full_url, headers=header)
    
    # if response is good
    if response.status_code == 200:
            
        # build a folder name
        folder = 'output/{}'.format(export_format)
        
        # if filter string was supplied, use it in the filename
        if filter_string:
            
            # build a filename
            filename = '{0}-{1}.{2}'.format(aws_region, filter_string, export_format)

        # don't include filter string
        else:

            # build a filename
            filename = '{0}.{1}'.format(aws_region, export_format)
        
        # combine the two to create a full path
        full_path = folder + '/' + filename
        
        # create the folder
        build_dir(folder)
        
        # if it's json, then save json file with indents
        if export_format == 'json':

            # json loads
            json_response = json.loads(response.content)
            
            if save:
                # save the response content to file
                save_json_file(full_path, json_response)

            return json_response
            
        # otherwise save bytes
        else:

            if save:        
                # save the response content to a file
                save_byte_file(full_path, response.content)

            return response.content

    # response not good
    else:
        
        # print the server response
        print(str(response.content))
        print()

        # raise an error
        raise ConnectionError('An issue with the CloudCraft API occurred')

        