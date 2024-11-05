#!/usr/bin/env python3

"""
This module provides a set of unit tests for validating the functionality
of a method designed to access values within nested dictionaries.
"""


from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
)
from unittest.mock import (
    patch,
    Mock,
)
import requests


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


class TestGetJson(unittest.TestCase):
    """
    validate the behavior of the utils.get_json function,
    ensuring it returns the expected results under various conditions.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, payload):
        """
        This method tests the utils.get_json function to verify that
        it correctly retrieves and returns JSON data as intended
        """
        with patch('requests.get') as mock_request:
            mock_response = Mock()
            mock_response.json.return_value = payload
            mock_request.return_value = mock_response

            result = get_json(test_url)

            mock_request.assert_called_once_with(test_url)
            self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
    This class serers to to validate the behavior of the memoization
    functionality, ensuring that repeated calls to a function with
    the same arguments return cached results instead of recomputing 
    the output.
    """

    def test_memoize(self):
        """
        This method tests the memoization feature to verify that
        it correctly caches results of function calls
        """
        class TestClass:
            
            def a_method(self):
                return 42
            
            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_a_method:
            test_obj = TestClass()
            result1 = test_obj.a_property
            result2 = test_obj.a_property
            
            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
