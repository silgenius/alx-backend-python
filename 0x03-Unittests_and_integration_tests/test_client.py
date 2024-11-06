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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Unit test for 'public_repos' in 'GithubOrgClient'.
        """

        payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes_dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratus",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }

        mock_get_json.return_value = payload['repos']

        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock
                ) as mock_public_repos_url:

            mock_public_repos_url.return_value = payload['repos_url']
            github_client = GithubOrgClient('google')
            github_client = github_client.public_repos()

            self.assertEqual(github_client, ["episodes_dart", "kratus"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
