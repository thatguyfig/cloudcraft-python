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
    

def get_dynamodb_data(dynamo_client,table_name: str):
    
    """Gets data from the AWS DynamoDB Service from the provided table and region."""

    # get the data from the table
    response = dynamo_client.scan(
        TableName=table_name
    )

    return response

def get_ec2_instance_private_ip(ec2_client, instance_id: str) -> str:

    """Gets the private IP of an EC2 instance based on instance ID"""
    response = ec2_client.describe_instances(
        InstanceIds=[
            instance_id,
        ],
    )

    # enter reservations
    for reservation in response['Reservations']:

        # enter instances
        for instance in reservation['Instances']:

            # extract private ip
            instance_ip = "pIP: " + instance['PrivateIpAddress']
        
            return instance_ip

def get_ec2_instance_public_ip(ec2_client, instance_id: str) -> str:

    """Gets the public IP of an EC2 instance based on instance ID"""
    response = ec2_client.describe_instances(
        InstanceIds=[
            instance_id,
        ],
    )

    # not all instances have a public ip
    try:

        # enter reservations
        for reservation in response['Reservations']:

            # enter instances
            for instance in reservation['Instances']:

                # extract the elastic ip
                instance_ip = "eIP: " + instance['PublicIpAddress']
            
                return instance_ip

    # otherwise
    except:

        # default no public ip value
        instance_ip = "eIP: N/A"

        return instance_ip

def get_ec2_instance_subnet_id(ec2_client, instance_id: str) -> str:

    """Gets the private IP of an EC2 instance based on instance ID"""

    # request for ec2 instance
    response = ec2_client.describe_instances(
        InstanceIds=[
            instance_id,
        ],
    )

    # enter reservations
    for reservation in response['Reservations']:

        # enter instances
        for instance in reservation['Instances']:

            # obtain instance SubnetId
            instance_subnet_id = instance['SubnetId']
    
            return instance_subnet_id


def get_rds_instance_subnet_ids(rds_client, instance_id: str):

    """Gets all the associated subnets with the RDS Instance"""

    # subnets
    assigned_subnets = []

    # make request
    response = rds_client.describe_db_instances(
        DBInstanceIdentifier=instance_id
    )

    # iterate over all subnets on the instance
    for subnet in response['DBInstances'][0]['DBSubnetGroup']['Subnets']:

        # add each of them to the subnet groups
        assigned_subnets.append(subnet['SubnetIdentifier'])

    return assigned_subnets