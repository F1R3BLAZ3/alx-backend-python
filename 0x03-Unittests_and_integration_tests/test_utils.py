#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the `access_nested_map` function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the `access_nested_map` function with various inputs.

        Parameters:
        - nested_map (dict): The nested dictionary to be accessed.
        - path (tuple): The path to the nested value.
        - expected_result: The expected result after accessing the nested value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_exception: Exception,
    ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
