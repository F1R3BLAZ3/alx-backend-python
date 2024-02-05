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

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key not found: 'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "Key not found: 'b'"),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception, expected_message):
        """
        Test that `access_nested_map` raises a KeyError
        with the expected message.

        Parameters:
        - nested_map (dict): The nested dictionary to be accessed.
        - path (tuple): The path to the nested value.
        - expected_exception: The expected exception type.
        - expected_message: The expected exception message.
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
