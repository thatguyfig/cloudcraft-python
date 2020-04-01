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

def add_text(bp_schema: dict, text_id: str, text_value: str, text_color='#ffffff', text_type='isotext', text_x=0, text_y=0, text_size=15):
    
    """Adds a text element to the Blueprint JSON"""
    
    # if there is no text element already in the blueprint
    if 'text' not in bp_schema['data']:
        
        # we create it
        bp_schema['data']['text'] = []
        
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



    

