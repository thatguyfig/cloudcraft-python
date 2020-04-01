# EXAMPLE3.PY
#
# Demonstration of the snapshot_aws_region capabilities
#
# This will create a new blueprint in CloudCraft using the response of the snapshot_aws_region. 
# Note that we disable the save parameter as we are not interested in saving the response to disk.
# Also note that this only works with the JSON format.

import cloudcraft

####################
# define the key
api_key = cloudcraft.load_json_file('config.json')['api_key']

# define aws account id
account_id = cloudcraft.load_json_file('config.json')['aws_account']

# define aws region
aws_region = "ap-southeast-1"

# define export format
export_format = "json"

# define the filter string to use
filter_string = "" # we are using blank string as we can't filter

# define the excluded types 
excluded_types = ["ebs", 'sns'] # removing EBS volumes

# filtered output blueprint name
blueprint_name = "Filtered Output Blueprint"

####################

# perform the snapshot and capture the response
response = cloudcraft.snapshot_aws_region(
    api_key=api_key,
    account_id=account_id,
    aws_region=aws_region,
    export_format=export_format,
    filter_string=filter_string,
    excluded_types=excluded_types,
    save=False
)

# nodes to remove
nodes_to_remove = ['ebs', 'sns', 'lambda', 's3', 'r53']

# filter the nodes
response = cloudcraft.remove_nodes_by_type(
    blueprint=response,
    types_to_remove=nodes_to_remove
)

# create a filename to store data in
filename = 'output/modified/{}.json'.format(aws_region)

# save data to the file
cloudcraft.save_json_file(filename=filename, data=response)

# override the blueprint name with what we want to call it
response['data']['name'] = blueprint_name

# create a new blueprint from filtered output
cloudcraft.create_blueprint(
    api_key=api_key,
    json_body=response
)