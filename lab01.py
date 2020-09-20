# import modules
import sys
from helper import *
from ruamel import yaml
import json
import xml.etree.ElementTree as ET

import xml.dom.minidom as MD


# Main function
if __name__ == "__main__":
    #################################
    #         Procedure 1           #
    #################################
    # Add print statement here
    print("DevNet")
    #################################
    #         Procedure 2           #
    #################################
    print('###################')
    print('####### YAML ######')
    print('###################')

    # Open the user.yaml file as read only
    with open('user.yaml', 'r') as stream:
        # load the stream using safe_load
        user_yaml = yaml.safe_load(stream)

    # Print the object type
    print("ype of user_yaml variable:")
    print(type(user_yaml))
    print('----------------------')

    # Iterate over the keys of the user_yaml and print them
    print('keys in user_yaml:')
    for key in user_yaml:
        print(key)
    print('----------------------')

    # Create a new instance of class User
    user = User()
    # Assign values from user_yaml to the object user
    user.id = user_yaml['id']
    user.first_name = user_yaml['first_name']
    user.last_name = user_yaml['last_name']
    user.birth_date = user_yaml['birth_date']
    user.address = user_yaml['address']
    user.score = user_yaml['score']


    # Print the user object
    print('User object:')
    print(user)

    #################################
    #         Procedure 3           #
    #################################
    print('###################')
    print('####### JSON ######')
    print('###################')

    # Create JSON structure from the user object
    user_json = json.dumps(user, default = serializeUser)

    # Print the created JSON structure
    print('Print user_json:')
    print(user_json)
    print('----------------------')