# import modules
import sys
from helper import *
from ruamel import yaml
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
