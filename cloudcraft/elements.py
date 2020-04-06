# ELEMENTS.PY
#
# All diagram elements

import requests
import json


def remove_nodes_by_type(blueprint: dict, types_to_remove: list):

    """Remove nodes from the provided blueprint and list of types."""

    # filter the current nodes, removing the ones we don't want
    nodes = [x for x in blueprint['data']['nodes'] if x['type'] not in types_to_remove]

    # reset some nodes
    blueprint['data']['nodes'] = nodes

    return blueprint

def list_blueprint_nodes(blueprint: dict, types_to_list=None):
    
    """List nodes from the provided blueprint and list of types. Returns JSON."""

    # access the blueprint and acquire all nodes
    nodes = blueprint['data']['nodes']

    # if types_to_list was supplied
    if types_to_list:
        
        # define an empty list
        matching_nodes = []

        # iterate over all the nodes
        for node in nodes:

            # check if the type matches
            if node['type'] in types_to_list:

                # then add it to the list
                matching_nodes.append(node)
        
        # finally return matching nodes
        return matching_nodes

    # else
    else:

        # stop iterating and just return all the nodes
        return nodes   

def list_blueprint_node_types(blueprint: dict):

    """Lists all the unique types for the provided blueprint"""

    # empty list
    node_types = []

    # iterate over all nodes in the blueprint
    for node in blueprint['data']['nodes']:

        # if the item isn't already in the list
        if node['type'] not in node_types:
            
            # add it to the list
            node_types.append(node['type'])

    return node_types

def add_text(bp_schema: dict, text_value: str, direction='down', relative_id=None, text_color='#000000', text_type='isotext', text_x=0, text_y=0, text_size=15, standing=False, outline=True):
    
    """Adds a text element to the Blueprint JSON"""
    
    # if there is no text element already in the blueprint
    if 'text' not in bp_schema['data']:
        
        # we create it
        bp_schema['data']['text'] = []

    # if there is a node to position this in relation to
    if relative_id:
        
        # build the text element
        text_obj = {
            'text': text_value,
            'type': text_type,
            'color': text_color,
            'mapPos': {
                "relTo": relative_id,
                "offset": [
                    text_x,
                    text_y
                ]
            },
            'textSize': text_size,
            'direction': direction,
            'standing': standing,
            'outline': outline
        }
    
    else:
        
        # build the text element
        text_obj = {
            'text': text_value,
            'type': text_type,
            'color': text_color,
            'mapPos': [
                text_x,
                text_y
            ],
            'textSize': text_size
        }

    # add the text element
    bp_schema['data']['text'].append(text_obj)
    
    # return the modified json
    return bp_schema

def add_node_group(bp_schema: dict, node_ids: list, group_name: str, group_colour: str) -> dict:

    """Adds the subnet groups to the diagram based on provided node IDs"""

    # create the group config
    group_config = {
            "type": "sg",
            "name": group_name,
            "nodes": node_ids,
            "color": {
                        "2d": group_colour,
                        "isometric": group_colour
            }
        }
    
    # add it to the existing group
    bp_schema['data']['groups'].append(group_config)

    # return it
    return bp_schema


def extract_node_arn(bp_schema: dict, node_arn_types=['ec2','rds']):

    """Extracts the Instance ARN of nodes that have it"""

    # empty list for results
    node_infos = []

    # extract the nodes from the schema
    nodes = bp_schema['data']['nodes']


    # iterate over the nodes
    for node in nodes:

        # if the node type is valid
        if node['type'] in node_arn_types:

            # get aws account
            aws_account = node['arn'].split(':')[4]

            # get aws region
            aws_region = node['arn'].split(':')[3]

            # default instance id
            instance_id = ""

            # if it's an ec2
            if node['type'] == 'ec2':
                instance_id = node['arn'].split('/')[1]

            if node['type'] == 'rds':
                instance_id = node['arn'].split(':')[6]

            node_info = {
                'id': node['id'],
                'type': node['type'],
                'arn': node['arn'],
                'instance_id': instance_id,
                'aws_account': aws_account,
                'aws_region': aws_region
            }

            assert instance_id != ""

            node_infos.append(node_info)

    return node_infos    

