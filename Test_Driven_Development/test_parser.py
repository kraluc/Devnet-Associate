import unittest
import sys, os
sys.path.append(os.path.join(os.path.curdir,'Test_Driven_Development'))
from ConfigurationParser import *

class TestParse(unittest.TestCase):

    cp = ConfigurationParser()
    expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
    expected_vlans = [100, 101]
    expected_ip_addresses = list(map(lambda vlan : f'10.10.{vlan}.1', expected_vlans))

    def test_parse_customer_name(self):

        parsed_names = self.cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(self.expected_names, parsed_names)


    def test_parse_customer_vlan(self):
        '''
            Validate vlans for all customers
        '''
        parsed_vlans = []
        for expected_vlan, customer_name in zip(
            self.expected_vlans,
            self.expected_names):
            parsed_vlans.append(self.cp.parseCustomerVlan(customer_name))
        self.assertEqual(self.expected_vlans, parsed_vlans)

    def test_parse_customer_ip_address(self):

        parsed_ip_addresses = []
        for expected_ip_addresses, customer_name in zip(
                self.expected_ip_addresses,
                self.expected_names):
            parsed_ip_addresses.append(self.cp.parseCustomerIPAddress(customer_name))
        self.assertEqual(self.expected_ip_addresses, parsed_ip_addresses)


if __name__ == "__main__":
    unittest.main()