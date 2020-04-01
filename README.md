# cloudcraft-python

A project for automated CloudCraft diagrams with AWS written with Python.

## Requirements

### Python Installation

Please make sure you have python 3.6 or above installed.

### Python Packages

To use this module, first you will need to install the dependent python packages using PIP. 

Use the below command to install all required modules

```python
pip install -r requirements.txt
```

## Usage

This module has been organised in such a way that related function / objects are stored in a related `.py` file. A massive amount of comments have been used throughout to help with others understanding the approach.

The structure can be seen below:

```
project
|  README.MD
|  requirements.txt
|  config copy.json
|
└───cloudcraft
|   |  __init__.py
|   |  accounts.py
|   |  aws.py
|   |  blueprint.py
|   |  elements.py
|   |  limits.py
|   |  snapshot.py
|   |  spacial.py
|   |  utils.py
|
└───examples
|   |  example1.py
|   |  example2.py
|   |  example3.py
|   |  example4.py
|   |  example5.py
|   |  example6.py
|   |  example7.py
|
└───output
|   |  existing/
|   |  json/
|   |  modified/
|   |  pdf/

```

- All code used to interact with cloudcraft is stored in `cloudcraft/`
- All examples used to demonstrate the usage of the functions are stored in `examples/`
- Configuration for your credentials must be made in `config.json`

In order to use this module, you must build from the functions provided. Take a look at the examples on guidance for using the module.

### Configure the config.json

Configure this JSON file to store the following:

1. Your cloudcraft API token
2. Your cloudcraft AWS account ID.

Make sure to rename the config file from `config copy.json` to `config.json`

### Build some code or use an example

Write your code, or run one of the examples by dragging it to the root of the project and running it using the below command for example:

```bash
python .\\example1.py
```

## Example Development

First, we have to import the module to use all of the functions / objects:

```python
import cloudcraft
```

Next, we need to load our `config.json` file so we can obtain credentials:

```python
# load the config.json
json_config = cloudcraft.load_json_file('config.json')

api_key = json_config['api_key']
account_id = json_config['aws_account']
```

Next, we need to decide what it is we want to do with CloudCraft. In this example we will look to snapshot an AWS region and export to PDF:

```python
# define aws region
aws_region = "ap-southeast-1"

# define export format
export_format = "pdf"

# define the filter string to use
filter_string = "" # we are using blank string as we don't want to filter

# define the excluded types 
excluded_types = ['ebs', 'lambda'] # removing EBS volumes and lambda functions
```

Now we have defined the parameters, we can call the `snapshot_aws_region()` function:

```python
# perform the snapshot
cloudcraft.snapshot_aws_region(
    api_key=api_key,
    account_id=account_id,
    aws_region=aws_region,
    export_format=export_format,
    filter_string=filter_string,
    excluded_types=excluded_types
)
```

Once you have saved and run this script, you will have a PDF created under the `output/pdf` directory. 

Open this in your browser to check the results.
