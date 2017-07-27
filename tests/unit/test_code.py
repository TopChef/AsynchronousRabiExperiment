"""
Contains unit tests for :mod:`code`
"""
from unittest import TestCase
from asynchronous_rabi_experiment.code import Flippable

class TestFlip(TestCase):
    """
    Tests that flipping a state successfully returns the
    expected result
    """
    def setUp(self):
        """
        Provide some test variables
        """
        self.flippable_thing = Flippable(Flippable.STATE_1)
        self.expected_result = Flippable.STATE_2

    def test_flip(self):
        """
        Tests that the function correctly flips the state
        """
        self.flippable_thing.flip()
        self.assertEqual(self.expected_result, self.flippable_thing.state) 

    def test_flippable_initialization(self):
        a = Flippable.STATE_1
        b = Flippable(Flippable.STATE_1)
        self.assertNotEqual(a, b)