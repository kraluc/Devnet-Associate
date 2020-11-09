import unittest
import sys, os
sys.path.append(os.path.join(os.path.curdir,'Test_Driven_Development'))
from ConfigurationParser import *

# TODO: Fix the decorator approach - currently failing
# See: https://medium.com/@vadimpushtaev/decorator-inside-python-class-1e74d23107f6

class TestParse(unittest.TestCase):

    cp = ConfigurationParser()
    expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
    expected_vlans = [100, 101]

    def test_parse_customer_name(self):
        parsed_names = self.cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(self.expected_names, parsed_names)

    def validate_result(self, customer):
        def validate_result(function):
            def wrapper(customer):
                self.assertEqual(customer, function(customer))
            return wrapper

    @ validate_result(expected_names[0])
    def test_parse_customer_vlan(customer_name):
        return  self.cp.parseCustomerVlan(customer_name)

    @ validate_result(expected_names[1])
    def test_parse_customer_vlan(customer_name):
        return  self.cp.parseCustomerVlan(customer_name)


if __name__ == "__main__":
    unittest.main()