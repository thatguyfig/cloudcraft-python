# EXAMPLE8.PY
#
# A demo of to make your own additions to specific nodes on a diagram.
#
# Here, we load a blueprint from local disk and then add text nodes on it for RDS and EC2 instances to show their instance sizes 
# from the information already contained in the blueprint.


import cloudcraft

# import the api_key
api_key = cloudcraft.load_json_file('config.json')['api_key']

# load blueprint from local
response = cloudcraft.load_blueprint_from_disk('output/json/ap-southeast-1.json')

# make modifications
text_color_hex = '#f59342'

# add the text elements to the diagram
modified = cloudcraft.add_instance_size_text(
    bp_schema=response,
    text_color=text_color_hex
)

# save the modified version to disk
cloudcraft.save_json_file('output/modified/ap-southeast-1.json', modified)

# update the title
modified['data']['name'] = 'ap-southeast-1 - Instance Sizes'

# create a blueprint
cloudcraft.create_blueprint(
    api_key=api_key,
    json_body=modified
)