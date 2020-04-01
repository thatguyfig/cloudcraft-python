# EXAMPLE6.PY
#
# Loading from a saved blueprint already captured. 
#
# You might want to do this to first export an existing snapshot and then make manual edits to then upload to the server.

import cloudcraft

# define the api key
api_key = cloudcraft.load_json_file('config.json')['api_key']

# define the path to the file
filepath = "output/existing/Test-Blueprint.json"

# load it from disk
blueprint = cloudcraft.load_blueprint_from_disk(filepath=filepath)

# if we found a blueprint
if blueprint:

    # here we need to check if there is an ID present - only existing blueprints have an ID
    if 'id' in blueprint:

        # then we need to update
        response = cloudcraft.update_blueprint(api_key=api_key, bp_id=blueprint['id'], json_body=blueprint)

    # otherwise 
    else:

        # need to create instead of update
        response = cloudcraft.create_blueprint(api_key=api_key, json_body=blueprint)


# then report the status
print(response.status_code)
print(response.content)