#!/usr/bin/env python3

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
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

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url.

        Use patch as a context manager to mock GithubOrgClient.org.
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        # Mock the payload returned by GithubOrgClient.org
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"}

        # Use patch to mock the org property and return the mock_payload
        with patch.object(
                GithubOrgClient, 'org',
                new_callable=PropertyMock,
                return_value=mock_payload
        ):
            github_client = GithubOrgClient("testorg")

            # Access the _public_repos_url property
            result = github_client._public_repos_url

            # Ensure that the result matches the expected value
            # from the mocked payload
            self.assertEqual(
                result, "https://api.github.com/orgs/testorg/repos")

    @patch('client.get_json', return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    @patch.object(
        GithubOrgClient,
        '_public_repos_url',
        new_callable=PropertyMock,
        return_value="https://api.github.com/orgs/testorg/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test GithubOrgClient.public_repos.

        Use @patch as a decorator to mock get_json and make it return a payload
        of your choice.
        Use patch as a context manager to mock
        GithubOrgClient._public_repos_url
        and return a value of your choice.
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json were called once.
        """
        github_client = GithubOrgClient("testorg")

        # Call public_repos method
        repos = github_client.public_repos()

        # Ensure that the list of repos is what you expect from
        # the chosen payload
        self.assertEqual(repos, ["repo1", "repo2"])

        # Ensure that the mocked property and the mocked get_json
        # were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/testorg/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Parametrize the test with the given inputs.

        Test GithubOrgClient.has_license with different inputs
        and expected results.
        """
        github_client = GithubOrgClient("testorg")

        # Call has_license method
        result = github_client.has_license(repo, license_key)

        # Ensure that the result matches the expected value
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
