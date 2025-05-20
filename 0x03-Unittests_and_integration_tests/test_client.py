#!/usr/bin/env python3
"""Unit and integration tests for the GithubOrgClient module.
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from typing import Dict
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org_returns_expected_data(self, org_name: str, expected: Dict, mock_get: MagicMock) -> None:
        """Test that GithubOrgClient.org returns correct org data."""
        mock_get.return_value = expected
        client_instance = GithubOrgClient(org_name)
        self.assertEqual(client_instance.org(), expected)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_repos_url_property(self) -> None:
        """Test that _public_repos_url returns the correct URL."""
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org_data:
            mock_org_data.return_value = {"repos_url": "https://api.github.com/users/google/repos"}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "https://api.github.com/users/google/repos")

    @patch("client.get_json")
    def test_fetching_public_repositories(self, mock_json: MagicMock) -> None:
        """Test that public_repos retrieves and returns repo names."""
        fake_repos = [
            {
                "name": "episodes.dart",
                "license": {"key": "bsd-3-clause"},
            },
            {
                "name": "kratu",
                "license": {"key": "apache-2.0"},
            },
        ]
        mock_json.return_value = fake_repos

        with patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/users/google/repos"
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["episodes.dart", "kratu"])
            mock_url.assert_called_once()
        mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "bsd-3-clause"}}, "bsd-3-clause", True),
        ({"license": {"key": "mit"}}, "apache-2.0", False),
    ])
    def test_license_check(self, repo_data: Dict, target_key: str, result: bool) -> None:
        """Test that has_license correctly identifies license keys."""
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo_data, target_key), result)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using fixtures."""

    @classmethod
    def setUpClass(cls) -> None:
        """Patch requests.get with a side effect to simulate API responses."""
        mock_routes = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def mocked_response(url):
            if url in mock_routes:
                return Mock(**{"json.return_value": mock_routes[url]})
            raise HTTPError

        cls.mock_get = patch("requests.get", side_effect=mocked_response)
        cls.mock_get.start()

    def test_repo_names_are_returned(self) -> None:
        """Ensure public_repos returns correct repository names."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_repo_filter_by_license(self) -> None:
        """Ensure public_repos filters repositories by license if specified."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop patching requests.get after tests are complete."""
        cls.mock_get.stop()
