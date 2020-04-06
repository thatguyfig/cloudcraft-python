# EXAMPLE10.PY
# 
# A demo of how to enrich further AWS info onto an already existing blueprint.
#
# This example shows how you can alter the grouping for subnet view instead of Security Groups

import cloudcraft

# load api key
api_key = cloudcraft.load_json_file('config.json')['api_key']

# define the blueprint name
blueprint_name = 'AWS - VPC'

# define the new blueprint name
new_blueprint_name = 'AWS - VPC (detailed)'

# get the current blueprint
blueprint_meta = cloudcraft.get_blueprint_by_name(blueprint_name=blueprint_name, api_key=api_key)

# get the current blueprint layout
blueprint = cloudcraft.get_blueprint_layout(api_key=api_key, bp_id=blueprint_meta[0]['id'], save=False)

# convert to json
blueprint = cloudcraft.get_json(blueprint)

# add instance ips
blueprint = cloudcraft.add_instance_ips(bp_schema=blueprint, text_color='#2e2e2e', text_x_offset=1, text_y_offset=.5)

# add instance sizes
blueprint = cloudcraft.add_instance_size_text(bp_schema=blueprint, text_color='#2e2e2e', text_x_offset=0, text_y_offset=1.3)

# add the subnet groups
blueprint = cloudcraft.add_subnet_groups(bp_schema=blueprint, group_colour='#000000', node_types=['ec2'])

# save to file
cloudcraft.save_json_file('output/modified/existing.json', data=blueprint)

# create the new blueprint
cloudcraft.create_blueprint(api_key=api_key, json_body=blueprint, blueprint_name=new_blueprint_name)
