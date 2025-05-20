#!/usr/bin/env python3
"""Module to unit test helper functions in utils.py
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence, Union

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""

    @parameterized.expand([
        ({"key": 10}, ("key",), 10),
        ({"outer": {"inner": 5}}, ("outer",), {"inner": 5}),
        ({"outer": {"inner": 5}}, ("outer", "inner"), 5),
    ])
    def test_valid_access(
        self,
        data: Mapping,
        keys: Sequence[str],
        expected_result: Union[int, Dict[str, Any]]
    ) -> None:
        """Test successful nested access with valid keys."""
        self.assertEqual(access_nested_map(data, keys), expected_result)

    @parameterized.expand([
        ({}, ("missing",), KeyError),
        ({"alpha": 3}, ("alpha", "beta"), KeyError),
    ])
    def test_invalid_access_raises(
        self,
        data: Mapping,
        keys: Sequence[str],
        expected_exc: Exception
    ) -> None:
        """Ensure KeyError is raised for invalid paths."""
        with self.assertRaises(expected_exc):
            access_nested_map(data, keys)


class TestGetJsonFunction(unittest.TestCase):
    """Unit tests for the get_json function."""

    @parameterized.expand([
        ("https://example.com", {"data": 123}),
        ("https://school.io", {"active": True}),
    ])
    def test_get_json_success(
        self,
        url: str,
        mock_response: Dict[str, Any]
    ) -> None:
        """Test that get_json returns the correct response payload."""
        mock_attrs = {"json.return_value": mock_response}
        with patch("requests.get", return_value=Mock(**mock_attrs)) as mock_get:
            result = get_json(url)
            self.assertEqual(result, mock_response)
            mock_get.assert_called_once_with(url)


class TestMemoizeFunction(unittest.TestCase):
    """Unit tests for the memoize decorator."""

    def test_memoization(self) -> None:
        """Test that memoize caches method results."""
        class Sample:
            def compute(self) -> int:
                return 99

            @memoize
            def cached_property(self) -> int:
                return self.compute()

        with patch.object(Sample, "compute", return_value=99) as mock_method:
            instance = Sample()
            self.assertEqual(instance.cached_property(), 99)
            self.assertEqual(instance.cached_property(), 99)
            mock_method.assert_called_once()
