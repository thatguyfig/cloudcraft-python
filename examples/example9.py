# EXAMPLE9.PY
#
# This example shows how to extract the relevant AWS ARNs for use in further calls to aws

import cloudcraft

# load api key
api_key = cloudcraft.load_json_file('config.json')['api_key']

# load blueprint from disk
blueprint = cloudcraft.load_blueprint_from_disk('output/json/ap-southeast-1.json')

# remove nodes from the diagram
nodes_to_remove = ['ebs', 'sns', 'lambda', 's3', 'r53']
blueprint = cloudcraft.remove_nodes_by_type(blueprint=blueprint, types_to_remove=nodes_to_remove)

# add instance sizes
blueprint_modified = cloudcraft.add_instance_size_text(bp_schema=blueprint, text_color='#0377fc', text_x_offset=1., text_y_offset=-.25)

# add instance ips
blueprint_modified = cloudcraft.add_instance_ips(bp_schema=blueprint_modified, text_color='#4e03fc', text_x_offset=-1., text_y_offset=.5)

# save updated version to disk
cloudcraft.save_json_file('output/modified/ap-southeast-1-ips.json', data=blueprint_modified)

# create a new blueprint
cloudcraft.create_blueprint(
    api_key=api_key,
    json_body=blueprint_modified
)