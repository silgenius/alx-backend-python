#!/usr/bin/env python3

"""
This module provides a set of unit tests for validating the functionality
of a method designed to access values within nested dictionaries.
"""


from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Inherits from unittest.TestCase and contains test methods specifically
    aimed at verifying the behavior of the nested map access method.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_accesss_nested_map(self, nested_map, path, expected):
        """This method tests the functionality of a specific method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
