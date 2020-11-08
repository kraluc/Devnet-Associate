#!/bin/env python

import unittest

class TestParse(unittest.TestCase):
    def test_parse_customer_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)
