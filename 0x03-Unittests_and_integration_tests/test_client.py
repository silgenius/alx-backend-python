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
    PropertyMock
)
from typing import Dict
import client


class TestGithubOrgClient(unittest.TestCase):
    """
    contains the test methods specifically designed to
    validate the functionality of the GithubOrgClient class
    """

    @parameterized.expand([
        ('google', {"data": "some_data"}),
        ('abc', {"data": "some_data"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, resp: Dict, mock_org: MagicMock):
        """
         It uses mocking techniques to simulate the behavior of external
         calls and verify the method's logic without actually invoking
         external services.
         """
        mock_org.return_value = resp

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, resp)
        mock_org.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
            )

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google'),
    ])
    def test_public_repos_url(self, org_name, payload):
        """
        Unit test for '_public_repos_url' in 'GithubOrgClient'.
        """
        with patch.object(
                GithubOrgClient,
                'org',
                new_callable=PropertyMock,
                return_value={
                    'repos_url': 'https://api.github.com/orgs/google'
                    }):
            client = GithubOrgClient(org_name)
            result = client._public_repos_url
            self.assertEqual(result, payload)

    @parameterized.expand([
        ('google', {'datas': ['data1', 'data2']}),  # Mock response for google
        ('abc', {'datas': ['data3', 'data']}),    # Mock response for abc
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, payload, mock_get_json):
        mock_get_json.return_value = payload
        url = f'https://api.github.com/orgs/{org_name}'

        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock
                ) as mock_public_repos_url:

            mock_public_repos_url.return_value = url
            result = client.get_json(url)
            github_client = GithubOrgClient(org_name)
            github_client = github_client._public_repos_url

            self.assertEqual(github_client, url)
            self.assertEqual(payload, result)
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
