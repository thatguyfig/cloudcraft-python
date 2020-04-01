# EXAMPLE4.PY
#
# A demonstration of how can use this to update an existing diagram using only the name

import cloudcraft
import json
####################
# define the key
api_key = cloudcraft.load_json_file('config.json')['api_key']

# blueprint name
blueprint_name = 'Test Blueprint'

# check for any matching blueprints
matching_blueprints = cloudcraft.get_blueprint_by_name(blueprint_name, api_key)

# default target to null
target = None

# if we found any
if matching_blueprints:

    # access the first and set as target
    target = matching_blueprints[0]

# if a target was obtained
if target:

    # get the blueprint and save it's layout locally
    response = cloudcraft.get_blueprint_layout(
        api_key=api_key,
        bp_id=target['id'],
        save=True
    )

    # convert to json
    json_response = cloudcraft.get_json(response.content)

    # modify something about the blueprint - the name
    json_response['data']['name'] = 'Test Blueprint - 30/03/2020'

    # update the existing blueprint
    cloudcraft.update_blueprint(
        api_key=api_key,
        bp_id=target['id'],
        json_body=json_response
    )

