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

def add_instance_size_text(bp_schema: dict, text_color='#f59342', text_x_offset=1., text_y_offset=.25):

    """Adds the EC2 instance size as text to the EC2 instance node"""

    # first, access the schema and obtain the 
    nodes = bp_schema['data']['nodes']

    # define the list of modified instance types
    nodes_with_instance_type = ['ec2', 'rds']

    # iterate over all nodes
    for node in nodes:
        
        # if the node is ec2 type
        if node['type'] in nodes_with_instance_type:

            # build the aws instance size
            instance_type = "{0}.{1}".format(node['instanceType'], node['instanceSize'])

            # capture the node id
            node_id = node['id']

            # create a text element for this node id
            bp_schema = add_text(
                bp_schema=bp_schema,
                text_value=instance_type,
                relative_id=node_id,
                text_x=text_x_offset,
                text_y=text_y_offset,
                text_color=text_color
            )

    # return the modified bp schema
    return bp_schema


    

