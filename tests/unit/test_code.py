"""
Contains unit tests for :mod:`code`
"""
import unittest
from asynchronous_rabi_experiment.code import add_one

class TestAddOne(unittest.TestCase):
    """
    Tests that adding one to a number successfully returns the
    expected result
    """
    def setUp(self):
        """
        Provide some test variables
        """
        self.number_to_add = 1
        self.expected_result = 2

    def test_add_one(self):
        """
        Tests that the function correctly adds one to
        the number to add.
        """
        result = add_one(self.number_to_add)
        self.assertEqual(self.expected_result, result) 

