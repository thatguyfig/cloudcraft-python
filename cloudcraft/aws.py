# AWS.PY
#
# All AWS related functions and code needed to interact with AWS.

import requests
import boto3
from boto3.session import Session

class ExcludedAwsRegions:

    """Class to store the excluded regions from AWS."""

    # define the regions you want to omit here
    regions = [
        'ap-east-1'
    ]


def list_regions(filter_regions=True):

    """Lists all the available AWS regions - is filtered by the ExcludedAwsRegions"""

    # create a boto session
    s = Session()

    # get all the regions from boto session
    regions = s.get_available_regions('ec2')

    # if filtering is enabled
    if filter_regions:

        # list comp boiiii
        regions = [x for x in regions if x not in ExcludedAwsRegions.regions]
    
    
    return regions

def create_aws_client(service: str, region: str):
    
    """Creates a client with AWS using boto3"""
    
    # build client
    client = boto3.client(service, region_name=region)
    
    return client
    

def get_dynamodb_data(table_name: str, table_region: str):
    
    """Gets data from the AWS DynamoDB Service from the provided table and region."""
    
    # build a client to dynamodb
    dynamo_client = create_aws_client('dynamodb', table_region)
    
    # get the data from the table
    response = dynamo_client.scan(
        TableName=table_name
    )
    
    return response
    



