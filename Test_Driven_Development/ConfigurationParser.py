import re
import os

FILE = os.path.join(os.path.abspath(os.path.curdir),'Test_Driven_Development','config.txt')

class ConfigurationParser:

    deviceConfig = open(FILE, 'r').read()

    def parseCustomerNames(self):
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        print(f'customer names: {customerNames}')
        return customerNames

    def parseCustomerVlan(self,customerName):
        " Note the atomic grouing ( +)"
        intPattern = (
            r"interface GigabitEthernet0\/0\.([0-9]+)\n  encapsulation " +
            r"dot1Q ([0-9]+)\n  ip vrf forwarding %s" % (customerName)
        )
        #print(f'customer vlan pattern {intPattern}')
        allCustomerSubInterfaces = re.search(intPattern, self.deviceConfig)
        print(f'vlan: {allCustomerSubInterfaces.group(1)}')
        return int(allCustomerSubInterfaces.group(1)) # return the 1st match

    def parseCustomerIPAddress(self, customerName):
        # It is important to make each section of the pattern greedy
        # = forcing a match with +
        byte = r"25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]"
        ipPattern = r"(" + (r"(%s)\." % byte) * 3 + r"(%s))" % byte # () for atomic result
        Pattern = r"(%s\n  ip address %s )" % (customerName, ipPattern)
        match = re.search(Pattern, self.deviceConfig).group(1)
        ip_match = re.search(ipPattern, match).group(1)
        print(f'{customerName} ip: {ip_match}')
        return ip_match
