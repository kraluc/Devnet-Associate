import unittest
import sys, os
sys.path.append(os.path.abspath('./Test_Driven_Development'))
from ConfigurationParser import *


class TestParse(unittest.TestCase):
    def test_parse_customer_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)

if __name__ == "__main__":
    unittest.main()