import re
import os

FILE = os.path.join(os.path.abspath(os.path.curdir),'Test_Driven_Development','config.txt')
print(FILE)

class ConfigurationParser:

    deviceConfig = open(FILE, 'r').read()

    def parseCustomerNames(self):
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        print(customerNames)
        return customerNames
