#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
            self, nested_map, path, expected_exception):
        """
        Tests `access_nested_map`'s exception raising.

        Parameters:
        - nested_map (dict): The nested dictionary to be accessed.
        - path (tuple): The path to the nested value.
        - expected_exception: The expected exception when the path is not found
        """
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the `get_json` function.
    """

    @patch('requests.get')
    def test_get_json(self, mock_get):
        """
        Test the `get_json` function with mocked requests.get.

        Parameters:
        - mock_get: Mock object for requests.get.
        """
        # Define test data
        test_url_1 = "http://example.com"
        test_payload_1 = {"payload": True}

        test_url_2 = "http://holberton.io"
        test_payload_2 = {"payload": False}

        # Set up the mock for requests.get
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload_1

        # Call get_json with the first set of test data
        result_1 = get_json(test_url_1)

        # Assert that requests.get was called exactly once with test_url_1
        mock_get.assert_called_once_with(test_url_1)

        # Assert that the output of get_json is equal to test_payload_1
        self.assertEqual(result_1, test_payload_1)

        # Reset the mock for requests.get
        mock_get.reset_mock()

        # Set up the mock for requests.get with different test data
        mock_get.return_value.json.return_value = test_payload_2

        # Call get_json with the second set of test data
        result_2 = get_json(test_url_2)

        # Assert that requests.get was called exactly once with test_url_2
        mock_get.assert_called_once_with(test_url_2)

        # Assert that the output of get_json is equal to test_payload_2
        self.assertEqual(result_2, test_payload_2)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the `memoize` decorator.
    """

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self) -> None:
        """
        Tests `memoize`'s output.
        """
        with patch.object(
                self.TestClass,
                "a_method",
                return_value=42,
        ) as memo_fxn:
            test_class = self.TestClass()
            # Access a_property as an attribute
            result_1 = test_class.a_property
            # Access a_property again as an attribute
            result_2 = test_class.a_property

            # Assert that a_method was called only once
            memo_fxn.assert_called_once()

            # Assert that the results are equal
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)


if __name__ == "__main__":
    unittest.main()
