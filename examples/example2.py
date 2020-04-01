# EXAMPLE2.PY
#
# Demonstration of the snapshot_aws_region capabilities
#
# This will save the response to disk under the 'output\' directory

import cloudcraft

####################
# define the key
api_key = cloudcraft.load_json_file('config.json')['api_key']

# define aws account id
account_id = cloudcraft.load_json_file('config.json')['aws_account']

# define aws region
aws_region = "ap-southeast-1"

# define export format
export_format = "pdf"

# define the filter string to use
filter_string = "" # we are using blank string as we don't want to filter

# define the excluded types 
excluded_types = ['ebs', 'lambda'] # removing EBS volumes

####################

# perform the snapshot
cloudcraft.snapshot_aws_region(
    api_key=api_key,
    account_id=account_id,
    aws_region=aws_region,
    export_format=export_format,
    filter_string=filter_string,
    excluded_types=excluded_types
)
