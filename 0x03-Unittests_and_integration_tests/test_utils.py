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
from unittest.mock import patch, Mock
import requests
from utils import get_json


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
