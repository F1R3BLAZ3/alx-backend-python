#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"org_key": "org_value"})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Parameters:
        - org_name (str): The name of the GitHub organization.
        - mock_get_json: Mock object for get_json function.
        """
        github_client = GithubOrgClient(org_name)

        # Access the property without calling it directly
        result = github_client.org

        # Ensure that get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name))

        # Ensure that the result matches the expected value
        self.assertEqual(result, {"org_key": "org_value"})


if __name__ == "__main__":
    unittest.main()
