#!/usr/bin/env python3

"""
This module contains a set of unit tests designed to validate
the behavior of the GithubOrgClient class, specifically its org method.
"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import (
    patch,
    Mock,
    MagicMock,
)


class TestiGithubOrgClient(unittest.TestCase):
    """
    contains the test methods specifically designed to
    validate the functionality of the GithubOrgClient class
    """

    @parameterized.expand([
        ('google', {"data": "some_data"}),
        ('abc', {"data": "some_data"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, resp, mock_org):
        """
         It uses mocking techniques to simulate the behavior of external
         calls and verify the method's logic without actually invoking
         external services.
         """
        mock_org.return_value = MagicMock(return_value=resp)

        client = GithubOrgClient(org_name)
        result = client.org
        mock_org.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
            )
