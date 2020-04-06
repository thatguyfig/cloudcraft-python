# EXTENSIONS.PY
#
# Adds further functionality to the cloudcraft blueprinting process.

from .aws import (
    create_aws_client, 
    get_ec2_instance_private_ip, 
    get_ec2_instance_public_ip, 
    get_ec2_instance_subnet_id, 
    get_rds_instance_subnet_ids
)
from .elements import (
    add_node_group, 
    add_text,
    extract_node_arn
)

def add_instance_size_text(bp_schema: dict, text_color='#f59342', text_x_offset=1., text_y_offset=.25):

    """Adds the instance size as text to the valid instance nodes"""

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

def add_instance_ips(bp_schema: dict, text_color='#f59342', text_x_offset=1., text_y_offset=-.25):

    """Adds the private IP as test to the valid instance nodes"""
    subnet_groups = {}
    
    # first obtain necessary node information
    node_info = extract_node_arn(bp_schema=bp_schema)

    
    # first access the schema
    for node in node_info:

        # if it's an ec2 instance
        if node['type'] == 'ec2':
            # create a client to aws
            ec2_client = create_aws_client(service='ec2',region=node['aws_region'])
            
            # get the private ip from AWS
            private_ip = get_ec2_instance_private_ip(ec2_client=ec2_client, instance_id=node['instance_id'])

            # get the public ip from AWS
            public_ip = get_ec2_instance_public_ip(ec2_client=ec2_client, instance_id=node['instance_id'])

            # get the subnet id from AWS
            subnet_id = get_ec2_instance_subnet_id(ec2_client=ec2_client, instance_id=node['instance_id'])


            # create a text element for this node id for private IP
            bp_schema = add_text(
                bp_schema=bp_schema,
                text_value=private_ip,
                relative_id=node['id'],
                text_x=text_x_offset,
                text_y=text_y_offset,
                text_color=text_color
            )

            # create a text element for this node id for public ip
            bp_schema = add_text(
                bp_schema=bp_schema,
                text_value=public_ip,
                relative_id=node['id'],
                text_x=text_x_offset,
                text_y=text_y_offset - .25,
                text_color=text_color
            )

            # create a text element for this node id for subnet id
            bp_schema = add_text(
                bp_schema=bp_schema,
                text_value=subnet_id,
                relative_id=node['id'],
                text_x=text_x_offset,
                text_y=text_y_offset - .5,
                text_color=text_color
            )
    
    # return updated bp_schema
    return bp_schema

def add_subnet_groups(bp_schema: dict, node_types: list, group_colour='#000000'):

    """Adds the private IP as test to the valid instance nodes"""

    subnet_groups = {}
    
    # first obtain necessary node information
    node_info = extract_node_arn(bp_schema=bp_schema)

    # iterate over each of the nodes
    for node in node_info:

        # if it's a type to process
        if node['type'] in node_types:

            # if it's an rds instance
            if node['type'] == 'rds':

                # build a client to rds
                rds_client = create_aws_client(service='rds', region=node['aws_region'])

                # get the rds instance info
                rds_instance_subnets = get_rds_instance_subnet_ids(rds_client=rds_client, instance_id=node['instance_id'])

                # iterate over all subnets on the instance
                for subnet in rds_instance_subnets:

                    # add each of them to the subnet groups
                    if subnet not in subnet_groups:

                        # create it
                        subnet_groups[subnet] = []
                    
                    # then add it
                    subnet_groups[subnet].append(node['id'])

            # if ec2
            if node['type'] == 'ec2':

                # build aws client
                ec2_client = create_aws_client(service='ec2', region=node['aws_region'])

                # get the subnet id from AWS
                subnet_id = get_ec2_instance_subnet_id(ec2_client=ec2_client, instance_id=node['instance_id'])

                # check for existence of of subnet_id
                if subnet_id not in subnet_groups:

                    # create it
                    subnet_groups[subnet_id] = []
                
                # add the node id
                subnet_groups[subnet_id].append(node['id'])

    # after looping for all nodes, we can now add node groups for subnets
    for subnet in subnet_groups.keys():

        # get subnet id
        subnet_id = subnet 

        # get group node ids
        group_ids = subnet_groups[subnet]

        # call the add groups function
        bp_schema = add_node_group(
            bp_schema=bp_schema,
            node_ids=group_ids,
            group_name=subnet_id,
            group_colour='#000000'
        )
    
    # return updated bp_schema
    return bp_schema