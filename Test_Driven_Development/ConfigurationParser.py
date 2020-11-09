import re
import os

FILE = os.path.join(os.path.abspath(os.path.curdir),'Test_Driven_Development','config.txt')

class ConfigurationParser:

    deviceConfig = open(FILE, 'r').read()

    def parseCustomerNames(self):
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        print(customerNames)
        return customerNames

    def parseCustomerVlan(self,customerName):
        intPattern = (
            r"interface GigabitEthernet0\/0\.([0-9]+)\n  encapsulation " +
            r"dot1Q ([0-9]+)\n  ip vrf forwarding %s" % (customerName)
        )
        print(f'customer vlan pattern {intPattern}')
        allCustomerSubInterfaces = re.search(intPattern, self.deviceConfig)
        print(allCustomerSubInterfaces)
        print(f'Full Match: {allCustomerSubInterfaces.group(0)}')
        print(f'first match: {allCustomerSubInterfaces.group(1)}')
        print(f'Second match: {allCustomerSubInterfaces.group(2)}') # should equal the 1st match
        return int(allCustomerSubInterfaces.group(1)) # return the 1st match
