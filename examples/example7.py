# EXAMPLE7.PY
#
# Working with the JSON to understand the elements present

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