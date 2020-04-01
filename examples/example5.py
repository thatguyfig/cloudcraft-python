# EXAMPLE5.PY
#
# Export an existing blueprint to JSON

import cloudcraft

# define the api key
api_key = cloudcraft.load_json_file('config.json')['api_key']

# define the target blueprint name
blueprint_name = "Test Blueprint"

# get the blueprint config using the name
response = cloudcraft.get_blueprint_by_name(
    blueprint_name=blueprint_name,
    api_key=api_key
)

# access first result
blueprint = response[0]

# get blueprint layout
response = cloudcraft.get_blueprint_layout(
    api_key=api_key,
    bp_id=blueprint['id']
)

# convert to json
json_response = cloudcraft.get_json(response.content)

# save response to file
cloudcraft.save_json_file('output/existing/Test-Blueprint.json', json_response)