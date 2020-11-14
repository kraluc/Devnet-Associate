#!/bin/env python
""" 13.3 Testing and Securing Applications
    4.5 Construct a Python Unit Test
"""
import sys, os
sys.path.append(os.path.join(os.path.curdir,'Unit_testing_45'))
import unittest
from is_greater import is_greater


class TestTools(unittest.TestCase):  # Derive a concrete child class from BASE class
    def setUp(self): # fixture method, run *before* the test method
        self.tools = Tools('admin') # not defined!

    # Define set of test methods - name must be prefixed with 'test', e.g. test_...
    def test_true_when_greater(self):
        self.assertTrue(self.tools.is_greater(5, 4))

    def test_user(self):
        self.assertEqual(self.tools.user, 'admin')

    def test_false_when_equal(self):
        self.assertFalse(self.tools.is_greater(5, 5))

    def tearDown(self): # fixture method, run *after* the test method
        self.tools.dispose()

if __name__ == "__main__":
    unittest.main()