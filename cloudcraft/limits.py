class CloudCraftAPILimit:
    
    """Class to store a bunch of settings related to the CloudCraftAPI limits specifically"""
    
    RequestRate = 30 # max 2 requests / 60s, therefore we use 30 to only allow 2 per min.
