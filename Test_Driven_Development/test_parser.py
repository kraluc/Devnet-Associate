import unittest
import sys, os
sys.path.append(os.path.join(os.path.curdir,'Test_Driven_Development'))
from ConfigurationParser import *

class TestParse(unittest.TestCase):
    cp = ConfigurationParser()
    def test_parse_customer_name(self):
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
        parsed_names = self.cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)
    def test_parse_customer_vlan(self):
        customer_name = 'CUSTOMER_A'
        expected_vlan = 100
        parsed_vlan = self.cp.parseCustomerVlan(customer_name)
        self.assertEqual(expected_vlan, parsed_vlan)

if __name__ == "__main__":
    unittest.main()