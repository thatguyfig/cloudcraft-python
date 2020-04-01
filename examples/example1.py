# EXAMPLE1.PY
#
# This example we will demonstrate each of the ways we can import the code

# RUNNING THIS WILL FAIL WITH API TOKEN ACCESS ISSUE #

#####################################
# Module relative (recommended) - i.e.
import cloudcraft

# then to use functions...
api_key = cloudcraft.load_json_file('config.json')['api_key']
cloudcraft.list_blueprints(api_key=api_key)

#####################################
# Import * (hacky)
from cloudcraft import *

# then to use functions
api_key = load_json_file('config.json')['api_key']
list_blueprints(api_key=api_key)

#####################################
# fully qualified name (too long + requires knowledge of object placement within files)
from cloudcraft.blueprint import list_blueprints, load_json_file

# then to use the functions
api_key = load_json_file('config.json')['api_key']
list_blueprints(api_key=api_key)