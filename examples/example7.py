# EXAMPLE7.PY
#
# Formation examples - very much experimental work in progress
#
# Here we load a bluepirnt from local disk, obtain all the ec2 nodes and create a square formation out of the nodes.
# 
# This is useful as sometimes you need to know how many elements will fit inside an even-sided shape. 
# 
# The Formation() class performs all the calculations on creation. This is useful for determining the amount of space elements may take up.

import cloudcraft

# define the path to the file
filepath = "output/existing/Test-Blueprint.json"

# load it from disk
blueprint = cloudcraft.load_blueprint_from_disk(filepath=filepath)

# print all the node types
print(cloudcraft.list_blueprint_node_types(blueprint))

# get all the nodes of the type 'ec2'
ec2_nodes = cloudcraft.list_blueprint_nodes(blueprint=blueprint, types_to_list=['ec2'])

# count the number of nodes
count = len(ec2_nodes)
print('Counted', count, 'nodes!')

# instantiate a formation
formation = cloudcraft.Formation(count=count, shape='square')

# print it's shape and count
formation.show()