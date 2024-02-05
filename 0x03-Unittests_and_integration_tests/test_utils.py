#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
