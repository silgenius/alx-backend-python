#!/usr/bin/env python3

"""
This module provides a set of unit tests for validating the functionality
of a method designed to access values within nested dictionaries.
"""


from parameterized import parameterized
from utils import access_nested_map
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
)


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
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence,
            expected: Any
            ):
        """This method tests the functionality of a specific method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            path: Sequence,
            error_type: KeyError
            ):
        """This method is designed to test the error-handling
        behavior of the nested map access method."""
        with self.assertRaises(error_type):
            access_nested_map(nested_map, path)
